import streamlit as st
import os
import certifi
import numpy as np
import time
from google import genai
from pypdf import PdfReader

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="SmartFinder AI", 
    page_icon="🔍", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fix SSL on Windows
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# Initialize API Client
API_KEY = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=API_KEY)

# --- 2. INITIAL KNOWLEDGE BASE ---
# We use Streamlit Session State to allow the document list to grow dynamically when PDFs are added
if "documents" not in st.session_state:
    st.session_state.documents = [
        "The 'DarkVisor' group targets financial institutions using Phishing emails.",
        "CVE-2026-999 is a critical vulnerability in Smart Toasters allowing remote code execution.",
        "SQL Injection attacks can be prevented by using Parameterized Queries in Python.",
        "The hacker known as 'GhostShell' was last seen using IP 192.168.1.50.",
        "To secure a Linux server, always disable Root login via SSH."
    ]

# --- 3. SMART AI HELPER FUNCTIONS ---
def get_embedding(text):
    try:
        result = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )
        return result.embeddings[0].values
    except Exception as e:
        st.error(f"API Connection Error: {e}")
        return []

# We cache embeddings dynamically based on the length of the document list
@st.cache_data
def get_all_document_embeddings(doc_list_tuple):
    # Streamlit caching works best with immutable types like tuples
    return [get_embedding(doc) for doc in doc_list_tuple]

def find_best_match(user_query):
    query_vector = get_embedding(user_query)
    if not query_vector:
        return "Sorry, I couldn't understand the meaning of your question.", 0.0
        
    # Convert session list to tuple for the cached function
    current_docs = tuple(st.session_state.documents)
    doc_embeddings = get_all_document_embeddings(current_docs)
    
    scores = []
    for doc_vector in doc_embeddings:
        if len(doc_vector) == 0:
            scores.append(-1.0)
            continue
        score = np.dot(query_vector, doc_vector)
        scores.append(score)
    
    best_index = np.argmax(scores)
    return st.session_state.documents[best_index], scores[best_index]

# --- 4. THE VISUAL STYLING ---
st.markdown("""
<style>
    .main-title { color: #1E3A8A; font-size: 36px; font-weight: 700; margin-bottom: 5px; }
    .subtitle { color: #4B5563; font-size: 15px; margin-bottom: 20px; }
    .guide-box {
        background-color: #EFF6FF;
        border-left: 5px solid #3B82F6;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    .guide-title { color: #1D4ED8; font-weight: 600; font-size: 16px; margin-bottom: 8px; }
</style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR DESIGN (The Document Hub) ---
with st.sidebar:
    st.markdown("<h2 style='color: #1E3A8A; margin-bottom: 0;'>🔍 SmartFinder</h2>", unsafe_allow_html=True)
    st.caption("Your Intelligent AI Document Assistant")
    st.markdown("---")
    
    st.write("🤖 **AI Engine:** Online & Ready")
    st.write(f"📄 **Knowledge Base:** {len(st.session_state.documents)} Sentences Memorized")
    st.markdown("---")
    
    # Live Document View
    with st.expander("📁 View Active Knowledge Base Files", expanded=True):
        st.markdown("<small>Here are the facts I currently remember. I will search through these to answer you!</small>", unsafe_allow_html=True)
        st.write("")
        for doc in st.session_state.documents:
            st.markdown(f"<div style='font-size: 13px; margin-bottom: 8px; color: #374151;'>📍 {doc}</div>", unsafe_allow_html=True)
            
    st.markdown("---")
    # Reset button to clear uploaded PDFs and return to baseline
    if st.button("🔄 Reset to Default Documents"):
        if "documents" in st.session_state:
            del st.session_state.documents
        st.cache_data.clear()
        st.rerun()

# --- 6. MAIN PANEL UI ---
st.markdown("<div class='main-title'>🔍 SmartFinder AI Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>A smart search terminal that understands concepts, not just words.</div>", unsafe_allow_html=True)

# NEW FEATURE: Dynamic Interactive Welcome Guide Box
with st.container():
    st.markdown(f"""
    <div class='guide-box'>
        <div class='guide-title'>👋 New here? Here is how to use your SmartFinder Dashboard:</div>
        <div style='font-size: 14px; color: #1F2937; line-height: 1.6;'>
            1️⃣ <b>Look at the Sidebar:</b> Open the dropdown menu on the left to see what text notes are already saved in the brain.<br>
            2️⃣ <b>Test the Core:</b> Type a question in the search bar below using completely different words (e.g., instead of copying a sentence exactly, try phrasing it like a casual conversation).<br>
            3️⃣ <b>Upload Your Own Knowledge:</b> Drop a custom PDF file into the upload zone below to watch the AI read, split, and immediately adapt to your own documents!
        </div>
    </div>
    """, unsafe_allow_html=True)

# NEW FEATURE: Document Uploader Component
st.markdown("### 📥 Expand the Knowledge Base")
uploaded_file = st.file_uploader("Upload a PDF document to add it to the AI's memory matrix", type=["pdf"])

if uploaded_file is not None:
    # Read text from PDF safely
    try:
        reader = PdfReader(uploaded_file)
        raw_text = ""
        for page in reader.pages:
            text_content = page.extract_text()
            if text_content:
                raw_text += text_content + " "
        
        # Split text into clean sentences based on periods
        new_sentences = [s.strip() + "." for s in raw_text.split('.') if len(s.strip()) > 15]
        
        # Check if these sentences are already imported to prevent duplicates
        fresh_sentences = [s for s in new_sentences if s not in st.session_state.documents]
        
        if fresh_sentences:
            st.session_state.documents.extend(fresh_sentences)
            # Clear cache so the system embeds the newly added lines on the next run
            st.cache_data.clear()
            st.success(f"🎉 Success! Read {len(fresh_sentences)} new sentences from **{uploaded_file.name}** and injected them into the sidebar search library!")
        else:
            st.info("ℹ️ This file's contents are already fully loaded or contain no readable text sentences.")
            
    except Exception as e:
        st.error(f"Could not read PDF structure: {e}")

st.markdown("---")

# --- 7. THE INTERACTIVE SEARCH CONSOLE ---
st.markdown("### 💬 Ask a Question")
query = st.text_input("What information are you trying to track down?", placeholder="e.g., Give me details on smart appliance safety updates...")

if query:
    with st.spinner("AI is analyzing text blocks and scanning data coordinates..."):
        time.sleep(0.6)
        best_doc, confidence = find_best_match(query)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("#### 📄 Best Matching Statement Found")
        st.info(f"**\"{best_doc}\"**")
    
    with col2:
        st.markdown("#### 📊 Accuracy rating")
        display_score = int(confidence * 100)
        if display_score > 100: display_score = 100
        if display_score < 0: display_score = 0
        
        if confidence > 0.4:  
            st.metric(label="Meaning Match", value=f"{display_score}%", delta="Strong Link")
        else:
            st.metric(label="Meaning Match", value=f"{display_score}%", delta="Low Link", delta_color="inverse")

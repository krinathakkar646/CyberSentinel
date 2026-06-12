import streamlit as st
import os
import certifi
import numpy as np
import time
import re
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

# Initialize API Client with error handling
try:
    API_KEY = st.secrets.get("GOOGLE_API_KEY")
    if not API_KEY:
        st.error("❌ GOOGLE_API_KEY not found in secrets. Please configure it in .streamlit/secrets.toml")
        st.stop()
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"❌ Failed to initialize API client: {e}")
    st.stop()

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
    """
    Get embedding for text using Google Gemini API.
    Returns normalized embedding vector or empty list on error.
    """
    if not text or not isinstance(text, str):
        return []
    
    try:
        result = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )
        embedding = result.embeddings[0].values
        # Normalize the embedding vector for better cosine similarity
        embedding_array = np.array(embedding)
        norm = np.linalg.norm(embedding_array)
        if norm > 0:
            embedding_array = embedding_array / norm
        return embedding_array.tolist()
    except Exception as e:
        st.error(f"⚠️ API Connection Error: {e}")
        return []

# We cache embeddings dynamically based on the length of the document list
@st.cache_data
def get_all_document_embeddings(doc_list_tuple):
    """
    Get embeddings for all documents in the knowledge base.
    Uses tuple for Streamlit caching compatibility.
    """
    return [get_embedding(doc) for doc in doc_list_tuple]

def find_best_match(user_query):
    """
    Find the best matching document for the user query using cosine similarity.
    Returns (document, confidence_score) tuple.
    """
    if not user_query or not isinstance(user_query, str):
        return "Sorry, I couldn't understand your question.", 0.0
    
    query_vector = get_embedding(user_query)
    if not query_vector or len(query_vector) == 0:
        return "Sorry, I couldn't understand the meaning of your question.", 0.0
        
    # Convert session list to tuple for the cached function
    current_docs = tuple(st.session_state.documents)
    doc_embeddings = get_all_document_embeddings(current_docs)
    
    scores = []
    for doc_vector in doc_embeddings:
        if not doc_vector or len(doc_vector) == 0:
            scores.append(-1.0)
            continue
        try:
            # Use normalized dot product (cosine similarity)
            score = float(np.dot(query_vector, doc_vector))
            scores.append(score)
        except Exception as e:
            st.warning(f"Error computing similarity: {e}")
            scores.append(-1.0)
    
    if not scores or all(s < 0 for s in scores):
        return "No suitable match found in the knowledge base.", 0.0
    
    best_index = np.argmax(scores)
    return st.session_state.documents[best_index], max(0.0, scores[best_index])

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
    st.markdown("""
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
        
        if not raw_text.strip():
            st.warning("⚠️ Could not extract text from the PDF. It may contain only images or be corrupted.")
        else:
            # Split text into clean sentences using regex for better sentence boundary detection
            # This handles periods, question marks, and exclamation marks
            sentence_pattern = r'[.!?]+(?:\s+|$)'
            raw_sentences = re.split(sentence_pattern, raw_text)
            
            # Clean and filter sentences
            new_sentences = []
            for s in raw_sentences:
                cleaned = s.strip()
                if len(cleaned) > 15:  # Only sentences with meaningful length
                    # Add appropriate punctuation if missing
                    if cleaned and not cleaned[-1] in '.!?':
                        cleaned += "."
                    new_sentences.append(cleaned)
            
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
        st.error(f"❌ Could not read PDF structure: {e}")

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
        # Confidence is now guaranteed to be between 0 and 1 (normalized embedding dot product)
        display_score = min(100, max(0, int(confidence * 100)))
        
        if confidence > 0.4:  
            st.metric(label="Meaning Match", value=f"{display_score}%", delta="Strong Link")
        else:
            st.metric(label="Meaning Match", value=f"{display_score}%", delta="Low Link", delta_color="inverse")

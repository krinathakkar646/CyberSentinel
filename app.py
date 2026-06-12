import streamlit as st
import os
import certifi
import numpy as np
import time
from google import genai

# --- 1. APP CONFIGURATION (Clean & Modern Branding) ---
st.set_page_config(
    page_title="SmartFinder AI", 
    page_icon="🔍", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fix SSL on Windows
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# 🚨 PASTE YOUR API KEY HERE
API_KEY = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=API_KEY)

# --- 2. THE KNOWLEDGE BASE (Your Uploaded Sentences) ---
documents = [
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

# Caching saves your API limits and speeds up the search drastically
@st.cache_data
def get_all_document_embeddings():
    return [get_embedding(doc) for doc in documents]

def find_best_match(user_query):
    query_vector = get_embedding(user_query)
    if not query_vector:
        return "Sorry, I couldn't understand the meaning of your question.", 0.0
        
    doc_embeddings = get_all_document_embeddings()
    
    scores = []
    for doc_vector in doc_embeddings:
        if len(doc_vector) == 0:
            scores.append(-1.0)
            continue
        # Math that measures how closely the "meanings" align
        score = np.dot(query_vector, doc_vector)
        scores.append(score)
    
    best_index = np.argmax(scores)
    return documents[best_index], scores[best_index]

# --- 4. THE NEW LOOK UI (Modern Corporate Tech Style) ---

# Custom styling for a bright, professional appearance
st.markdown("""
<style>
    /* Styling the main title banner */
    .main-title {
        color: #1E3A8A; /* Deep Trustworthy Blue */
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .subtitle {
        color: #4B5563; /* Slate Gray */
        font-size: 16px;
        margin-bottom: 25px;
    }
    /* Highlight box for information cards */
    .info-card {
        background-color: #F3F4F6;
        border-left: 5px solid #3B82F6;
        padding: 15px;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar - Beginner Friendly Info Panel
with st.sidebar:
    st.markdown("<h2 style='color: #1E3A8A; margin-bottom: 0;'>🔍 SmartFinder</h2>", unsafe_allow_html=True)
    st.caption("Your Intelligent AI Document Assistant")
    st.markdown("---")
    
    # System stats rewritten in regular English
    st.write("🤖 **AI Engine:** Ready")
    st.write("📄 **Documents Loaded:** 5 Files Connected")
    st.markdown("---")
    
    # Option 2 Integration - Completely beginner friendly explanation
    with st.expander("📁 View the files I can read", expanded=True):
        st.markdown("<small>I have read and memorized these 5 specific security notes. You can ask me about them using your own words!</small>", unsafe_allow_html=True)
        st.write("")
        for doc in documents:
            st.markdown(f"<div style='font-size: 13px; margin-bottom: 8px; color: #374151;'>📍 {doc}</div>", unsafe_allow_html=True)
            
    st.markdown("---")
    st.caption("Powered by Smart Meaning-Based Search")

# Main Interface Header
st.markdown("<div class='main-title'>🔍 SmartFinder AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask a question in normal, everyday English. Our AI will understand what you mean and find the perfect match—even if you don't use exact words!</div>", unsafe_allow_html=True)

# Clean Text Input
query = st.text_input("💬 What are you looking for today?", placeholder="e.g., Which hacker group is going after banks?")

if query:
    # Friendly waiting indicator
    with st.spinner("AI is reading through your files to find the right answer..."):
        time.sleep(0.8) # Quick smooth transition
        best_doc, confidence = find_best_match(query)
    
    # Laying out the results clearly in two columns
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 📄 Best Matching Document Found")
        st.info(f"**\"{best_doc}\"**")
    
    with col2:
        st.markdown("### 📊 Search Confidence")
        # Turn raw mathematical dot product into a friendly, readable percentage
        display_score = int(confidence * 100)
        if display_score > 100: display_score = 100
        if display_score < 0: display_score = 0
        
        if confidence > 0.4:  
            st.metric(label="Meaning Match Accuracy", value=f"{display_score}%", delta="Strong Match")
        else:
            st.metric(label="Meaning Match Accuracy", value=f"{display_score}%", delta="Weak Match", delta_color="inverse")

    # Kept the deep analysis but gave it an easy description
    with st.expander("🔬 Technical View (How the AI saw your question)"):
        q_emb = get_embedding(query)
        if q_emb:
            st.write("The AI converted your sentence into these structural mathematical coordinates to calculate the meaning:")
            st.write(q_emb[:10])
            st.caption("...showing first 10 dimensions of the meaning-vector.")
        else:
            st.write("Could not retrieve mathematical vector logic.")

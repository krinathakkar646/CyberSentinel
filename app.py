import streamlit as st
import os
import certifi
import numpy as np
import time
from google import genai

# --- 1. APP CONFIGURATION (The Branding) ---
st.set_page_config(
    page_title="CyberSentinel", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fix SSL on Windows
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# 🚨 PASTE YOUR API KEY HERE
API_KEY = "YOUR API KEY"
client = genai.Client(api_key=API_KEY)

# --- 2. THE KNOWLEDGE BASE ---
documents = [
    "The 'DarkVisor' group targets financial institutions using Phishing emails.",
    "CVE-2026-999 is a critical vulnerability in Smart Toasters allowing remote code execution.",
    "SQL Injection attacks can be prevented by using Parameterized Queries in Python.",
    "The hacker known as 'GhostShell' was last seen using IP 192.168.1.50.",
    "To secure a Linux server, always disable Root login via SSH."
]

# --- 3. HELPER FUNCTIONS ---
def get_embedding(text):
    try:
        result = client.models.embed_content(
            model="text-embedding-004",
            contents=text
        )
        return result.embeddings[0].values
    except Exception as e:
        st.error(f"API Connection Error: {e}")
        return []

def find_best_match(user_query):
    query_vector = get_embedding(user_query)
    doc_embeddings = [get_embedding(doc) for doc in documents]
    
    scores = []
    for doc_vector in doc_embeddings:
        score = np.dot(query_vector, doc_vector)
        scores.append(score)
    
    best_index = np.argmax(scores)
    return documents[best_index], scores[best_index]

# --- 4. THE UI LAYOUT (Cyberpunk Style) ---

# Sidebar Control Panel
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/9203/9203764.png", width=100)
    st.title("CyberSentinel v1.0")
    st.markdown("---")
    st.write("🟢 **System Status:** ONLINE")
    st.write("🛡️ **Security Level:** HIGH")
    st.write("📂 **Database:** 5 Records Loaded")
    st.markdown("---")
    st.caption("Powered by Google Gemini RAG")

# Main Interface
st.title("🛡️ CyberSentinel: Threat Intelligence Hub")
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    color: #00FF00;
}
</style>
""", unsafe_allow_html=True)

st.markdown("Welcome, Agent. Ask the Neural Core about known threats, CVEs, or hacker groups.")

# Chat Input with a "Hacker" feel
query = st.text_input("🔍 ENTER QUERY PARAMETERS:", placeholder="e.g., Who is targeting financial banks?")

if query:
    # A fake progress bar to look like it's "Thinking"
    with st.spinner("Decrypting Neural Pathways..."):
        time.sleep(1) # Dramatic pauseimport streamlit as st
import os
import certifi
import numpy as np
import time
from google import genai

# --- 1. APP CONFIGURATION (The Branding) ---
st.set_page_config(
    page_title="CyberSentinel", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fix SSL on Windows
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# 🚨 PASTE YOUR API KEY HERE
API_KEY = "AIzaSyD57Vvvp3HcmU1AgKp7QQrEkAHC64Q4Bog"
client = genai.Client(api_key=API_KEY)

# --- 2. THE KNOWLEDGE BASE ---
documents = [
    "The 'DarkVisor' group targets financial institutions using Phishing emails.",
    "CVE-2026-999 is a critical vulnerability in Smart Toasters allowing remote code execution.",
    "SQL Injection attacks can be prevented by using Parameterized Queries in Python.",
    "The hacker known as 'GhostShell' was last seen using IP 192.168.1.50.",
    "To secure a Linux server, always disable Root login via SSH."
]

# --- 3. HELPER FUNCTIONS ---
def get_embedding(text):
    try:
        result = client.models.embed_content(
            model="text-embedding-004",
            contents=text
        )
        return result.embeddings[0].values
    except Exception as e:
        st.error(f"API Connection Error: {e}")
        return []

def find_best_match(user_query):
    query_vector = get_embedding(user_query)
    doc_embeddings = [get_embedding(doc) for doc in documents]
    
    scores = []
    for doc_vector in doc_embeddings:
        score = np.dot(query_vector, doc_vector)
        scores.append(score)
    
    best_index = np.argmax(scores)
    return documents[best_index], scores[best_index]

# --- 4. THE UI LAYOUT (Cyberpunk Style) ---

# Sidebar Control Panel
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/9203/9203764.png", width=100)
    st.title("CyberSentinel v1.0")
    st.markdown("---")
    st.write("🟢 **System Status:** ONLINE")
    st.write("🛡️ **Security Level:** HIGH")
    st.write("📂 **Database:** 5 Records Loaded")
    st.markdown("---")
    st.caption("Powered by Google Gemini RAG")

# Main Interface
st.title("🛡️ CyberSentinel: Threat Intelligence Hub")
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    color: #00FF00;
}
</style>
""", unsafe_allow_html=True)

st.markdown("Welcome, Agent. Ask the Neural Core about known threats, CVEs, or hacker groups.")

# Chat Input with a "Hacker" feel
query = st.text_input("🔍 ENTER QUERY PARAMETERS:", placeholder="e.g., Who is targeting financial banks?")

if query:
    # A fake progress bar to look like it's "Thinking"
    with st.spinner("Decryptinimport streamlit as st
import os
import certifi
import numpy as np
import time
from google import genai

# --- 1. APP CONFIGURATION (The Branding) ---
st.set_page_config(
    page_title="CyberSentinel", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fix SSL on Windows
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# 🚨 PASTE YOUR API KEY HERE
API_KEY = "AIzaSyD57Vvvp3HcmU1AgKp7QQrEkAHC64Q4Bog"
client = genai.Client(api_key=API_KEY)

# --- 2. THE KNOWLEDGE BASE ---
documents = [
    "The 'DarkVisor' group targets financial institutions using Phishing emails.",
    "CVE-2026-999 is a critical vulnerability in Smart Toasters allowing remote code execution.",
    "SQL Injection attacks can be prevented by using Parameterized Queries in Python.",
    "The hacker known as 'GhostShell' was last seen using IP 192.168.1.50.",
    "To secure a Linux server, always disable Root login via SSH."
]

# --- 3. HELPER FUNCTIONS ---
def get_embedding(text):
    try:
        result = client.models.embed_content(
            model="text-embedding-004",
            contents=text
        )
        return result.embeddings[0].values
    except Exception as e:
        st.error(f"API Connection Error: {e}")
        return []

def find_best_match(user_query):
    query_vector = get_embedding(user_query)
    doc_embeddings = [get_embedding(doc) for doc in documents]
    
    scores = []
    for doc_vector in doc_embeddings:
        score = np.dot(query_vector, doc_vector)
        scores.append(score)
    
    best_index = np.argmax(scores)
    return documents[best_index], scores[best_index]

# --- 4. THE UI LAYOUT (Cyberpunk Style) ---

# Sidebar Control Panel
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/9203/9203764.png", width=100)
    st.title("CyberSentinel v1.0")
    st.markdown("---")
    st.write("🟢 **System Status:** ONLINE")
    st.write("🛡️ **Security Level:** HIGH")
    st.write("📂 **Database:** 5 Records Loaded")
    st.markdown("---")
    st.caption("Powered by Google Gemini RAG")

# Main Interface
st.title("🛡️ CyberSentinel: Threat Intelligence Hub")
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    color: #00FF00;
}
</style>
""", unsafe_allow_html=True)

st.markdown("Welcome, Agent. Ask the Neural Core about known threats, CVEs, or hacker groups.")

# Chat Input with a "Hacker" feel
query = st.text_input("🔍 ENTER QUERY PARAMETERS:", placeholder="e.g., Who is targeting financial banks?")

if query:
    # A fake progress bar to look like it's "Thinking"
    with st.spinner("Decrypting Neural Pathways..."):
        time.sleep(1) # Dramatic pause
        best_doc, confidence = find_best_match(query)
    
    # Display Results in columns
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📝 Intelligence Report")
        st.info(f"{best_doc}")
    
    with col2:
        st.subheader("📊 Confidence")
        # Color code the confidence score
        if confidence > 0.7:
            st.metric(label="Match Accuracy", value=f"{int(confidence * 100)}%", delta="High Certainty")
        else:
            st.metric(label="Match Accuracy", value=f"{int(confidence * 100)}%", delta="Low Certainty", delta_color="inverse")

    with st.expander("🔎 View Vector Analysis"):
        st.write(f"Query Vector (First 10 Dims): {str(get_embedding(query)[:10])}...")g Neural Pathways..."):
        time.sleep(1) # Dramatic pause
        best_doc, confidence = find_best_match(query)
    
    # Display Results in columns
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📝 Intelligence Report")
        st.info(f"{best_doc}")
    
    with col2:
        st.subheader("📊 Confidence")
        # Color code the confidence score
        if confidence > 0.7:
            st.metric(label="Match Accuracy", value=f"{int(confidence * 100)}%", delta="High Certainty")
        else:
            st.metric(label="Match Accuracy", value=f"{int(confidence * 100)}%", delta="Low Certainty", delta_color="inverse")

    with st.expander("🔎 View Vector Analysis"):
        st.write(f"Query Vector (First 10 Dims): {str(get_embedding(query)[:10])}...")
        best_doc, confidence = find_best_match(query)
    
    # Display Results in columns
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📝 Intelligence Report")
        st.info(f"{best_doc}")
    
    with col2:
        st.subheader("📊 Confidence")
        # Color code the confidence score
        if confidence > 0.7:
            st.metric(label="Match Accuracy", value=f"{int(confidence * 100)}%", delta="High Certainty")
        else:
            st.metric(label="Match Accuracy", value=f"{int(confidence * 100)}%", delta="Low Certainty", delta_color="inverse")

    with st.expander("🔎 View Vector Analysis"):
        st.write(f"Query Vector (First 10 Dims): {str(get_embedding(query)[:10])}...")

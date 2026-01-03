# 🛡️ CyberSentinel: AI Threat Intelligence Dashboard

> **"A Semantic Search Engine for Cybersecurity using Retrieval-Augmented Generation (RAG)."**

**CyberSentinel** is a Next-Gen Threat Intelligence interface that replaces standard keyword search with **Vector Embeddings**. It allows security analysts to query a database using *natural language concepts* rather than exact matches.


## 🧠 The Problem vs. The Solution

| Standard Search (Ctrl+F) | 🛡️ CyberSentinel (RAG) |
| :--- | :--- |
| Searches for **exact words** (e.g., "Toaster"). | Searches for **meaning** (e.g., "Kitchen Appliance"). |
| Fails if the hacker uses slang/synonyms. | Understands context and intent. |
| Returns zero results for vague queries. | Returns the statistically closest match. |

## ⚡ Key Features
- **Neural Memory:** Uses Google's `text-embedding-004` model to convert text into high-dimensional vectors.
- **Cosine Similarity Engine:** Calculates the mathematical distance between user queries and stored threat logs using `NumPy`.
- **Live Confidence Scoring:** Displays a real-time percentage of how "sure" the AI is about the match.
- **Cyberpunk UI:** Built with **Streamlit** for a modern, dark-mode security dashboard experience.

## 🛠️ Tech Stack
- **Python 3.12**
- **Streamlit** (Frontend Interface)
- **Google Gemini API** (Embeddings Model)
- **NumPy** (Vector Mathematics)

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/krinathakkar646/cyber-sentinel.git](https://github.com/krinathakkar646/cyber-sentinel.git)
cd cyber-sentinel

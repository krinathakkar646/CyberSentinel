# 🔍 SmartFinder AI Dashboard

An intelligent, beginner-friendly document search engine built with **Streamlit** and **Google Gemini AI**. Unlike traditional keyword searching (`Ctrl + F`), SmartFinder AI uses semantic artificial intelligence to understand the **meaning and intent** behind your questions, successfully pulling relevant text answers even if you don't use exact matching words.

---

## 🚀 Key Features

* **Interactive Setup Guide:** A clean, welcoming walkthrough box at the top of the interface to guide non-technical users step-by-step.
* **Live PDF Upload Matrix:** Drag and drop your own custom PDF documents directly into the dashboard. The app dynamically reads, splits, and memorizes your text data instantly.
* **Semantic Vector Matching:** Powered by the modern `gemini-embedding-001` infrastructure to compare abstract concepts instead of raw characters.
* **Live Sidebar Database Viewer:** Users can glance at an expandable file library on the left sidebar to see exactly what facts the AI has memorized.
* **Performance Optimization:** Utilizes caching loops (`@st.cache_data`) to prevent redundant API overhead and maintain instant lookup times.

---

## 🛠️ Technology Stack

* **Frontend UI:** [Streamlit](https://streamlit.io/) (Python Web Framework)
* **AI Engine:** [Google GenAI SDK](https://github.com/google/generative-ai-python) (`gemini-embedding-001`)
* **Document Processing:** `pypdf` (Text extraction utility)
* **Vector Mathematics:** `numpy` (Dot product calculation arrays)

---

## 📋 Pre-requisites & Setup

To run this dashboard locally on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone (https://github.com/krinathakkar646/CyberSentinel.git)
cd CyberSentinel

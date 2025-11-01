# 💬 Gurleen's Personal Chatbot

A smart, personalized chatbot built to answer questions about **Gurleen** — her projects, education, skills, certifications, and more.  
It uses **vector-based retrieval** with **FAISS** and **Sentence Transformers**, combined with **Cohere’s Command R+ LLM** for natural and human-like responses.

---

## ✨ Overview

This chatbot is designed as a **personal portfolio assistant**, allowing anyone to interactively learn about Gurleen’s professional background.  
When a user asks a question, the system retrieves relevant information from a **JSON knowledge base** (containing Gurleen’s details), and the **Cohere LLM** generates a natural, context-aware response.

---

## 🧠 How It Works

1. **User Query → Embedding:**  
   The question entered by the user is converted into a numerical vector using a **Sentence Transformer model** (`all-MiniLM-L6-v2`).

2. **Similarity Search with FAISS:**  
   The query embedding is compared with stored embeddings (of Gurleen’s data). FAISS finds the most relevant entries.

3. **LLM Response Generation (Cohere):**  
   The retrieved data is passed to **Cohere’s Command R+ model**, which refines the answer — ensuring it sounds natural, concise, and contextually accurate.

4. **Streamlit Interface:**  
   The entire chat experience runs through a sleek and modern **Streamlit** UI with interactive chat history and quick-question buttons.

---

## 🚀 Features

- 💡 **Personalized Q&A:**  
  Ask anything about Gurleen — projects, certifications, education, or experiences.

- 🧩 **Hybrid Intelligence:**  
  Combines **FAISS-based retrieval** with **Cohere LLM** reasoning for relevant and human-like responses.

- 🎨 **Streamlit Frontend:**  
  Clean, interactive UI with persistent chat history and pre-set question buttons.

- 📄 **JSON Knowledge Base:**  
  Stores structured personal data (prompts and responses).

- 🔍 **Semantic Search:**  
  Ensures that even similar or loosely phrased questions retrieve correct answers.

---

## 🧰 Tech Stack

| Layer | Tools/Frameworks |
|-------|------------------|
| **Frontend** | Streamlit |
| **Backend Logic** | Python |
| **Vector Embeddings** | Sentence Transformers (`all-MiniLM-L6-v2`) |
| **Vector Store** | FAISS |
| **LLM** | Cohere Command R+ |
| **Data Format** | JSON |

## 🗂️ Project Structure

```
│
├── app.py                # Streamlit frontend
├── chatbot.py            # Backend logic (FAISS + Cohere integration)
├── mydata.json           # Gurleen's personal data (prompt-response pairs)
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

```
🧑‍💻 Created by Gurleen
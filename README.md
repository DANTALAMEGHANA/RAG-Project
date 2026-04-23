# 📌 RAG-Based Customer Support Assistant (LangGraph + HITL)

## 🚀 Project Overview
This project implements a **Retrieval-Augmented Generation (RAG)** based Customer Support Assistant that answers user queries using information from a PDF knowledge base.

Instead of generating random responses, the system retrieves relevant information from documents and provides accurate, context-aware answers.

---

## 🎯 Features
- 📄 PDF-based knowledge ingestion  
- ✂️ Text chunking for efficient processing  
- 🔎 Semantic search using embeddings  
- 🧠 Vector database (FAISS) for fast retrieval  
- 🔄 Workflow orchestration using LangGraph  
- 🤝 Human-in-the-Loop (HITL) fallback mechanism  
- 💬 Interactive CLI-based chatbot  

---

## 🧩 System Architecture
User Query
↓
LangGraph Workflow
↓
Retriever (FAISS)
↓
Relevant Chunks
↓
Response Generation
↓
Answer / HITL Escalation


---

## ⚙️ Tech Stack

- Python  
- LangChain  
- LangGraph  
- FAISS (Vector Database)  
- Sentence Transformers  
- PyPDF  

---

## 🔄 Workflow

1. Load PDF document  
2. Split into chunks  
3. Convert chunks into embeddings  
4. Store embeddings in FAISS  
5. User enters query  
6. Retrieve top relevant chunks  
7. Generate response  
8. If no result → escalate to human  

---

## 📂 Project Structure
rag-project/
│
├── backend/
│ ├── main.py
│
├── data/
│ └── sample.pdf
│
├── docs/
│ ├── HLD.pdf
│ ├── LLD.pdf
│ └── Technical_Documentation.pdf
│
└── README.md


---

## ⚠️ Challenges Faced

- Environment setup issues  
- Vector database compatibility (ChromaDB → FAISS switch)  
- Ensuring relevant retrieval  

---

## 📈 Future Enhancements

- Add LLM-based answer generation  
- Support multiple documents  
- Build web UI  
- Add conversation memory  
- Deploy as API  

---

## 📌 Key Learnings

- Understanding of RAG pipeline  
- Working with embeddings & vector databases  
- Workflow orchestration using LangGraph  
- Designing scalable AI systems  

---

## 🙌 Acknowledgement

This project was developed as part of an AI/ML learning program to gain hands-on experience in building real-world AI systems.

---

## 🔗 Author

**YMeghana Dantala**

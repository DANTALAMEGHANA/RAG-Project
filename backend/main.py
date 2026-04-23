from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langgraph.graph import StateGraph

print("Program started...")

# -----------------------------
# Step 1: Load PDF
# -----------------------------
loader = PyPDFLoader("../data/sample.pdf")
documents = loader.load()

# -----------------------------
# Step 2: Split into chunks
# -----------------------------
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

print("Chunks created:", len(chunks))

# -----------------------------
# Step 3: Create embeddings
# -----------------------------
embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# -----------------------------
# Step 4: Store in FAISS
# -----------------------------
db = FAISS.from_documents(chunks, embedding)

# -----------------------------
# Step 5: LangGraph process function
# -----------------------------
def process(state):
    query = state["query"]

    # get top 3 relevant chunks
    results = db.similarity_search(query, k=3)

    # HITL condition
    if len(results) == 0:
        return {"answer": "Escalated to human support."}

    # combine results
    context = "\n\n".join([doc.page_content for doc in results])

    answer = f"""
Customer Support Assistant:

Based on the document, here is the answer:

{context}
"""

    return {"answer": answer}

# -----------------------------
# Step 6: Build LangGraph
# -----------------------------
graph = StateGraph(dict)

graph.add_node("process", process)

graph.set_entry_point("process")

app = graph.compile()

# -----------------------------
# Step 7: Ask question (interactive)
# -----------------------------
while True:
    query = input("\nEnter your question (type 'exit' to stop): ")

    if query.lower() == "exit":
        break

    result = app.invoke({"query": query})

    print("\nAnswer:\n")
    print(result["answer"])
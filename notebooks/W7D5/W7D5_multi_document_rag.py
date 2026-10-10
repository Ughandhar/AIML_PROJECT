# W7D5: Import required libraries

import os
import time
import mlflow
import chromadb

from pathlib import Path
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import StateGraph, START, END

print("Core libraries imported successfully!")


# Use a local SQLite database for MLflow tracking
mlflow.set_tracking_uri(f"sqlite:///{(OUTPUT_DIR / 'mlflow.db').resolve().as_posix()}")


mlflow.set_experiment("W7D5_Multi_Document_RAG")


# W7D5: Create sample documents

documents = {
    "python.txt": """
Python is a programming language used in automation, data science,
machine learning, and artificial intelligence.
""",
    "rag.txt": """
Retrieval-Augmented Generation (RAG) retrieves relevant documents
and uses their information to generate context-based answers.
""",
    "mlops.txt": """
MLOps combines machine learning, software engineering, and operations.
It helps track experiments, evaluate models, and manage deployments.
"""
}

for filename, content in documents.items():
    (DATA_DIR / filename).write_text(content.strip(), encoding="utf-8")

print(f"Created {len(documents)} sample documents.")
print("Files:", ", ".join(documents.keys()))


# W7D5: Load documents from files

loaded_documents = []

for file_path in DATA_DIR.glob("*.txt"):
    loaded_documents.append({
        "source": file_path.name,
        "text": file_path.read_text(encoding="utf-8")
    })

print("Documents loaded:", len(loaded_documents))

for document in loaded_documents:
    print("-", document["source"])


# W7D5: Load and split documents

from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_DIR = Path("notebooks/W7D5/documents")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=30
)

chunks = []

for file_path in sorted(DATA_DIR.glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")

    for chunk in text_splitter.split_text(text):
        chunks.append({
            "source": file_path.name,
            "text": chunk
        })

print("Documents processed:", len(list(DATA_DIR.glob("*.txt"))))
print("Total chunks:", len(chunks))
print("First chunk:", chunks[0]["text"])


# W7D5: Initialize Ollama embeddings

from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Test the embedding model
test_embedding = embeddings.embed_query("What is RAG?")

print("Embedding model: nomic-embed-text")
print("Embedding dimensions:", len(test_embedding))
print("Embedding test successful!")


# W7D5: Store document chunks in ChromaDB

import chromadb

client = chromadb.PersistentClient(
    path="notebooks/W7D5/chroma_db"
)

collection = client.get_or_create_collection(
    name="w7d5_documents"
)

for index, chunk in enumerate(chunks):
    collection.upsert(
        ids=[str(index)],
        documents=[chunk["text"]],
        metadatas=[{"source": chunk["source"]}]
    )

print("Vector store created successfully!")
print("Stored chunks:", collection.count())


# W7D5: Recreate ChromaDB collection with correct embeddings

client.delete_collection("w7d5_documents")

collection = client.create_collection(
    name="w7d5_documents",
    metadata={"hnsw:space": "cosine"}
)

for index, chunk in enumerate(chunks):
    collection.upsert(
        ids=[str(index)],
        embeddings=[embeddings.embed_query(chunk["text"])],
        documents=[chunk["text"]],
        metadatas=[{"source": chunk["source"]}]
    )

print("Vector store rebuilt successfully!")
print("Stored chunks:", collection.count())


# W7D5: Retrieve relevant document chunks

query = "What is RAG?"

results = collection.query(
    query_embeddings=[embeddings.embed_query(query)],
    n_results=2
)

for source, text in zip(
    results["metadatas"][0],
    results["documents"][0]
):
    print("Source:", source["source"])
    print("Content:", text)
    print("-" * 40)


# W7D5: Define the RAG workflow

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class RAGState(TypedDict):
    question: str
    context: str

def retrieve_documents(state: RAGState):
    results = collection.query(
        query_embeddings=[
            embeddings.embed_query(state["question"])
        ],
        n_results=2
    )

    context = "\n".join(results["documents"][0])

    return {"context": context}

workflow = StateGraph(RAGState)

workflow.add_node("retrieve", retrieve_documents)
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", END)

rag_app = workflow.compile()

print("LangGraph retrieval workflow created successfully!")


# W7D5: Test the LangGraph workflow

question = "What is RAG?"

result = rag_app.invoke({
    "question": question,
    "context": ""
})

print("Question:", question)
print("\nRetrieved context:")
print(result["context"])


# W7D5: Generate an answer from retrieved context

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2.5:3b")

context = result["context"]

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question: {question}

Answer:
"""

answer = llm.invoke(prompt)

print("Question:", question)
print("\nGenerated answer:")
print(answer)


# W7D5: Log the RAG experiment with MLflow

import mlflow

with mlflow.start_run(run_name="W7D5_RAG_Test"):
    mlflow.log_param("llm_model", "qwen2.5:3b")
    mlflow.log_param("embedding_model", "nomic-embed-text")
    mlflow.log_param("document_count", 3)
    mlflow.log_metric("retrieved_chunks", len(result["context"].split("\n")))

    mlflow.log_text(question, "question.txt")
    mlflow.log_text(answer, "generated_answer.txt")

print("MLflow experiment logged successfully!")


# W7D5: Evaluate the generated answer

expected_keywords = ["retrieval", "documents", "context"]

answer_lower = answer.lower()

matched_keywords = [
    word for word in expected_keywords
    if word in answer_lower
]

score = len(matched_keywords) / len(expected_keywords)

print("Expected keywords:", expected_keywords)
print("Matched keywords:", matched_keywords)
print(f"Keyword match score: {score:.2f}")
print("Evaluation completed!")


# W7D5: Save evaluation results

from pathlib import Path

OUTPUT_DIR = Path("notebooks/W7D5/outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

evaluation_text = f"""
W7D5 RAG Evaluation

Question: {question}
Expected keywords: {expected_keywords}
Matched keywords: {matched_keywords}
Keyword match score: {score:.2f}

Generated answer:
{answer}
"""

evaluation_file = OUTPUT_DIR / "evaluation_results.txt"
evaluation_file.write_text(evaluation_text.strip(), encoding="utf-8")

print("Evaluation results saved successfully!")
print("File:", evaluation_file)


# W7D5: Run basic pipeline tests

assert len(chunks) == 3, "Document chunk count is incorrect"
assert collection.count() == 3, "Vector store count is incorrect"
assert result["context"], "Retrieved context is empty"
assert answer.strip(), "Generated answer is empty"
assert score == 1.0, "Keyword evaluation failed"

print("All 5 RAG pipeline tests passed!")


# W7D5: Save test evidence

test_results = {
    "document_count": len(chunks),
    "stored_chunks": collection.count(),
    "retrieval_working": bool(result["context"]),
    "answer_generation_working": bool(answer.strip()),
    "keyword_score": score,
    "tests_passed": 5
}

test_file = OUTPUT_DIR / "test_results.txt"

with test_file.open("w", encoding="utf-8") as file:
    for name, value in test_results.items():
        file.write(f"{name}: {value}\n")

print("Test evidence saved successfully!")
print("File:", test_file)


# W7D5: Log a second RAG interaction

question_2 = "What is MLOps?"

result_2 = rag_app.invoke({
    "question": question_2,
    "context": ""
})

prompt_2 = f"""
Answer using only the context below.

Context:
{result_2["context"]}

Question: {question_2}

Answer:
"""

answer_2 = llm.invoke(prompt_2)

with mlflow.start_run(run_name="W7D5_RAG_Interaction_2"):
    mlflow.log_param("llm_model", "qwen2.5:3b")
    mlflow.log_text(question_2, "question.txt")
    mlflow.log_text(answer_2, "generated_answer.txt")

print("Interaction 2 logged successfully!")
print("Question:", question_2)
print("Answer:", answer_2)


# W7D5: Save interaction evidence

interaction_file = OUTPUT_DIR / "interaction_evidence.txt"

interaction_text = f"""
W7D5 RAG Interaction Evidence

Interaction 1
Question: {question}
Answer: {answer}

Interaction 2
Question: {question_2}
Answer: {answer_2}
"""

interaction_file.write_text(
    interaction_text.strip(),
    encoding="utf-8"
)

print("Both interactions saved successfully!")
print("Interactions recorded: 2")
print("File:", interaction_file)


# W7D5: Verify saved evidence files

required_files = [
    "evaluation_results.txt",
    "test_results.txt",
    "interaction_evidence.txt"
]

for filename in required_files:
    file_path = OUTPUT_DIR / filename
    print(f"{filename}: {'OK' if file_path.exists() else 'MISSING'}")

print("Evidence verification completed!")


# W7D5: Create the self-review checklist

from pathlib import Path

review = """W7D5 — MULTI-DOCUMENT RAG SELF-REVIEW

[✓] Created and loaded three sample documents
[✓] Split documents into chunks
[✓] Generated 768-dimensional Ollama embeddings
[✓] Stored and retrieved chunks using ChromaDB
[✓] Built the retrieval workflow using LangGraph
[✓] Generated answers using Ollama qwen2.5:3b
[✓] Logged experiment data using MLflow
[✓] Evaluated the answer using keyword matching
[✓] Passed five basic pipeline tests
[✓] Saved evaluation and test evidence
[✓] Logged two RAG interactions

Pending:
[ ] Complete Ragas evaluation
[ ] Final verification and Git workflow
"""

review_file = Path("notebooks/W7D5/SELF_REVIEW.md")
review_file.write_text(review, encoding="utf-8")

print("Self-review checklist saved successfully!")
print("File:", review_file)


# W7D5: Check Ragas availability

try:
    import ragas
    print("Ragas is available!")
    print("Version:", ragas.__version__)
except Exception as error:
    print("Ragas import failed:")
    print(type(error).__name__, "-", error)


# W7D5: Check Ragas and LangChain package versions

from importlib.metadata import version, PackageNotFoundError

packages = [
    "ragas",
    "langchain",
    "langchain-core",
    "langchain-community",
    "langchain-google-vertexai",
]

for package in packages:
    try:
        print(f"{package}: {version(package)}")
    except PackageNotFoundError:
        print(f"{package}: Not installed")


# W7D5: Locate the installed Ragas source file

from pathlib import Path
from importlib.metadata import distribution

ragas_path = Path(distribution("ragas").locate_file("ragas/llms/base.py"))

print("Ragas source file:", ragas_path)
print("File exists:", ragas_path.exists())


# W7D5: Inspect Ragas imports

with ragas_path.open("r", encoding="utf-8") as file:
    lines = file.readlines()

for number, line in enumerate(lines[:25], start=1):
    print(f"{number}: {line.rstrip()}")


# W7D5: Check Vertex AI integration availability

from importlib.util import find_spec

print(
    "Google Vertex AI integration:",
    find_spec("langchain_google_vertexai")
)


# W7D5: Record Ragas compatibility status

from pathlib import Path

OUTPUT_DIR = Path("notebooks/W7D5/outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ragas_status = """W7D5 Ragas Compatibility Check

Installed Ragas version: 0.4.3
Issue: Ragas imports a missing langchain_community Vertex AI module.
Replacement integration: Not installed.
Status: Pending compatibility fix and evaluation.
Core RAG pipeline: Working.
"""

status_file = OUTPUT_DIR / "ragas_status.txt"
status_file.write_text(ragas_status, encoding="utf-8")

print("Ragas status recorded.")
print("File:", status_file)


# W7D5: Verify project files

from pathlib import Path

project_dir = Path("notebooks/W7D5")

required_files = [
    project_dir / "W7D5_multi_document_rag.ipynb",
    project_dir / "SELF_REVIEW.md",
    project_dir / "outputs/evaluation_results.txt",
    project_dir / "outputs/test_results.txt",
    project_dir / "outputs/interaction_evidence.txt",
    project_dir / "outputs/ragas_status.txt",
]

for file_path in required_files:
    status = "OK" if file_path.exists() else "MISSING"
    print(f"{file_path}: {status}")


# W7D5: Find the saved notebook

from pathlib import Path

search_dir = Path("notebooks/W7D5")

for file_path in search_dir.rglob("*.ipynb"):
    print("Notebook found:", file_path)


# W7D5: Check the notebook working directory

import os

print("Current working directory:")
print(os.getcwd())

print("\nW7D5 folder exists:")
print(os.path.exists("notebooks/W7D5"))


# W7D5: Find the saved notebook

from pathlib import Path

search_dir = Path("W7D5")

print("Folder exists:", search_dir.exists())

for file_path in search_dir.rglob("*.ipynb"):
    print("Notebook found:", file_path)


# W7D5: Inspect folder contents

from pathlib import Path

folder = Path("W7D5")

for item in folder.iterdir():
    print("Folder:" if item.is_dir() else "File:", item.name)


# W7D5: Verify the main Python script

from pathlib import Path

script_path = Path("W7D5/W7D5_multi_document_rag.py")

print("Script exists:", script_path.exists())

if script_path.exists():
    print("Script size:", script_path.stat().st_size, "bytes")

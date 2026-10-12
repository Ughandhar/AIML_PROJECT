from fastapi import FastAPI

app = FastAPI(
    title="Production RAG API",
    description="W8D1 MLOps assignment API",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Production RAG API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}

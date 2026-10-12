# W7D2 — Haystack Retrieval Evaluation

## Evaluation Summary

The Haystack retrieval pipeline was evaluated using 10 questions across 5 indexed PDF documents.

| Method | Questions | Correct | Accuracy |
|---|---:|---:|---:|
| BM25 + Reader | 10 | 10/10 | 100% |
| Dense + Reader | 10 | 10/10 | 100% |

## BM25 Retrieval

BM25 with the extractive Reader answered all 10 evaluation questions correctly.

**Result: 10/10 — 100%**

## Dense Retrieval

Dense Retrieval using the sentence-transformers/all-MiniLM-L6-v2 embedding model answered all 10 evaluation questions correctly.

**Result: 10/10 — 100%**

## Comparison

Both methods achieved the same accuracy on this small evaluation dataset.

- **BM25:** lexical/keyword-based retrieval
- **Dense Retrieval:** semantic embedding-based retrieval

## Conclusion

BM25 and Dense Retrieval both achieved 100% accuracy on the evaluated questions. Dense Retrieval provides semantic matching through embeddings, while BM25 relies primarily on lexical keyword matching.

# W7D3 — LlamaIndex Retrieval Evaluation

## Overview

Built a LlamaIndex document querying pipeline using Ollama embeddings and a local collection of five robotics and AI text documents.

## Documents

- pid_controller.txt
- ros2.txt
- computer_vision.txt
- autonomous_vehicles.txt
- machine_learning.txt

## LlamaIndex Pipeline

- LlamaIndex version: 0.14.25
- Embedding model: Ollama 
omic-embed-text
- Embedding dimensions: 768
- Index: VectorStoreIndex
- LLM: Ollama qwen2.5:3b
- QueryEngine: Successfully created

## Query Evaluation

10 queries were executed and verified against the source documents.

- Queries tested: 10
- Answers successfully generated: 10/10
- Source topics covered: PID control, ROS 2, computer vision, autonomous vehicles, and machine learning.

## ChromaDB Integration

ChromaDB was connected using the LlamaIndex Chroma vector store integration.

- ChromaDB version: 1.5.9
- LlamaIndex Chroma integration: 0.6.0
- ChromaDB-backed VectorStoreIndex: Successfully created
- ChromaDB QueryEngine: Successfully created

## Latency Comparison

The same 10 queries were executed using both indexing approaches.

| Method | Average Latency |
|---|---:|
| Original VectorStoreIndex | 9.2559 seconds |
| ChromaDB | 14.5930 seconds |
| Difference | 5.3371 seconds |
| Latency Change | +57.66% |

### Result

In this local 10-query test, the ChromaDB-backed pipeline had a higher average latency than the original in-memory VectorStoreIndex.

## Conclusion

W7D3 successfully demonstrated document indexing with LlamaIndex and Ollama embeddings, QueryEngine-based question answering, ChromaDB integration, repeated query evaluation, and latency comparison.

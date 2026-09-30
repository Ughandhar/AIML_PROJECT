# W5D6 LLM Routing Strategy

## Objective

Reduce LLM API cost and unnecessary external requests by routing queries according to complexity, privacy, repetition, and context size.

## Routing Rules

| Query Type | Recommended Route | Reason |
|---|---|---|
| Simple factual robotics question | Local LLM | Low complexity and no external API cost |
| Repeated FAQ / known question | Semantic Cache | Return cached answer when similarity >= 0.92 |
| Private or sensitive local documents | Local LLM + RAG | Keeps document processing local |
| Complex reasoning task | API LLM | Use a stronger model when local quality is insufficient |
| Large RAG context | Compress + API LLM | Reduce input tokens before API request |
| High-volume repeated requests | Semantic Cache + Local LLM | Reduce repeated inference and API usage |
| Time-sensitive external information | API LLM | Use an API workflow when current external information is required |

## Semantic Cache

The semantic cache stores 20 Q&A pairs and uses a cosine similarity threshold of 0.92.

Observed results:

- Exact matching query: similarity = 1.0000 → Cache HIT
- Paraphrased query: similarity = 0.4680 → Cache MISS

## Prompt Compression

A robotics RAG context was compressed using LLMLingua-2 at rate=0.4.

- Original tokens: 2,289
- Compressed tokens: 818
- Tokens saved: 1,471
- Token reduction: 64.26%
- Key-topic retention: 93.75%

The topic-retention result is a keyword/topic-retention proxy, not a complete semantic quality evaluation.

## Cost Optimization

Using the project assumption of ₹85 per USD:

- Baseline RAG cost: ₹1.3553
- Optimized RAG cost: ₹0.7302
- Cost saved: ₹0.6252 per request
- Cost reduction: 46.13%

The cost reduction is lower than the token reduction because output-token cost remained unchanged in the comparison.

## Recommended Pipeline

1. Check semantic cache.
2. If cache similarity >= 0.92, return the cached answer.
3. If the query is simple, use the local LLM.
4. For private documents, use local RAG.
5. For large RAG contexts, compress the context before an API request.
6. Use an API LLM for complex reasoning or tasks requiring current external information.
7. Track input/output tokens and daily cost.

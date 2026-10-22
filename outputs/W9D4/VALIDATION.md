# W9D4 — Validation Report

## 1. LangChain Chain
- Status: PASS
- Pipeline: PromptTemplate → OllamaLLM → StrOutputParser
- Tests completed: 5/5

## 2. Conversation Memory
- Status: PASS
- Implementation: ConversationBufferMemory
- Turns tested: 5
- Recall verified: Robot name (Atlas) and purpose (agricultural work)
- Note: Deprecation warnings were emitted by legacy memory components.

## 3. Tools
- Web search: PASS — retrieved results about ROS 2.
- Calculator: PASS — (25 * 4) + 10 = 110.

## 4. Agent Tasks
1. Cost calculation: PASS — 8 × ₹450 + ₹1200 = ₹4800.
2. ROS documentation search: PASS — summary returned; exact source claims were not independently verified.
3. Robot average speed: PASS — 150 m / 30 s = 5 m/s.

## 5. Evidence
- `evaluation_results.json`

## 6. Limitations
- ConversationBufferMemory and InMemoryChatMessageHistory emitted deprecation warnings.
- The web-search agent's summary needs independent checking against the official ROS 2 documentation.
- Tests were run using the local Ollama model `qwen2.5:3b`.

## Overall Result
Core chain, five-turn memory, both tools, and three agent tasks were exercised successfully.

# W10D1 Validation — LangGraph Stateful Agent Graphs

## Implementation
- Created a three-node LangGraph workflow: classify, route, and respond.
- Added conditional routing based on classification.
- Used LangGraph InMemorySaver checkpointing for human review.
- Implemented interrupt, human input, and resume.

## Test Results
- Five predefined inputs tested: 5/5 passed.
- Greeting route: passed.
- Technical-support route: passed.
- Question route: passed.
- General-response route: passed.
- Human-review pause: passed.
- Human-review resume: passed.
- Saved evaluation JSON parsed and all evidence assertions passed.

## Evidence
- `outputs/W10D1/evaluation_results.json`
- `notebooks/W10D1_langgraph_stateful_agent_graphs.ipynb`

## Limitations
- Classification uses keyword rules rather than an LLM.
- In-memory checkpoints do not persist across process restarts.
- Five examples are a small test set and do not establish broad classification accuracy.

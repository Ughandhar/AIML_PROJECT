# W9D2 Validation Report

## Environment
- CrewAI: 1.15.28
- LLM: Ollama `qwen2.5:3b`
- Web search: DuckDuckGo via `ddgs`

## Verified results
- Baseline Researcher → Writer → Reviewer crew completed.
- Baseline review evidence saved to `outputs/W9D2/baseline_review.txt`.
- DuckDuckGo returned usable titles, URLs, and snippets when the `duckduckgo` backend was selected explicitly.
- Web-enhanced review evidence saved to `outputs/W9D2/web_enhanced_review.txt`.
- Safe calculation test: `(1200 * 0.15) + 40` returned `220.0`.
- Safety test: `__import__('os').getcwd()` was rejected.
- Comparison evidence saved to `outputs/W9D2/evaluation_comparison.json`.

## Evaluation limitation
The enhanced output is shorter than the baseline, but output length alone does not establish improved quality. Compare the actual reviewer feedback before claiming improvement. Confirm from the crew logs that the researcher actually invoked its tools.

## Remaining checks
- Review the notebook from top to bottom and confirm its saved outputs.
- Complete the required CIA Full Stack Mentor Mode interactions and retain genuine evidence.
- Complete the self-review before final submission.

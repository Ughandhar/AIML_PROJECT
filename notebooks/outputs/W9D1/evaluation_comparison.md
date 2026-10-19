# W9D1 CrewAI Evaluation

## Baseline and web-enhanced comparison

- Baseline review length: 3314 characters
- Web-enhanced review length: 2901 characters
- Outputs differ: True
- Baseline verdict: NEEDS IMPROVEMENT
- Web-enhanced verdict: NEEDS IMPROVEMENT

## Evidence collected

- Research Analyst produced non-empty research notes.
- Research notes contained 5 URL-like references.
- Direct live-search test returned search results with titles, URLs, and snippets.
- Research domains overlapping with the direct search results:
  blog.unitlab.ai, geeksforgeeks.org, smashingrobotics.com

## Limitations

- The direct search test confirms the search tool works.
- Shared domains do not prove that the Research Analyst called the tool during the crew run.
- Both runs require human verification of factual accuracy and source quality.
- A changed output does not by itself demonstrate improved quality.
- Both reviews should be assessed against the task requirements before claiming success.

## Conclusion

The sequential crew executed and produced review outputs. The live-search tool works independently and the research notes contain source references. Tool invocation during the crew run and any improvement in research quality remain unverified.

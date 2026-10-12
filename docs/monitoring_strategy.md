# Production RAG API — Monitoring Strategy

## 1. Metrics to Track

- API availability: health endpoint success rate.
- Latency: average and p95 response time.
- Errors: HTTP 5xx rate and failed requests.
- Retrieval quality: Recall@K, Precision@K, and relevance scores on a labelled evaluation set.
- Generation quality: answer correctness, faithfulness, and groundedness.
- Resource usage: CPU, memory, and container restarts.
- Cost: tokens consumed and cost per request.
- Data quality: document freshness and changes in input data.

## 2. Alert Thresholds

These are initial example thresholds. Tune them using baseline measurements.

| Metric | Example alert threshold |
|---|---|
| API availability | Below 99.5% over 5 minutes |
| p95 latency | Above 1 second for 5 minutes |
| HTTP 5xx error rate | Above 5% for 5 minutes |
| Container health | Repeated health-check failures |
| Retrieval quality | More than 10% degradation from baseline |
| Token cost | Above the configured daily budget |
| Data freshness | Important documents exceed their freshness SLA |

## 3. Monitoring and Response

- Collect structured request logs, latency, status codes, and resource metrics.
- Avoid logging secrets, credentials, or sensitive user content.
- Use dashboards to compare current metrics with a known baseline.
- Investigate alerts before restarting services or changing models.
- Record incidents, root causes, and corrective actions.

## 4. Retraining and Re-indexing Triggers

- Re-index when the document corpus changes or becomes stale.
- Evaluate the system when retrieval relevance or answer faithfulness degrades.
- Consider retraining or adapting a model only when sustained evaluation results show a model-related issue and suitable updated data is available.
- Validate candidate changes against a fixed evaluation dataset before deployment.
- Roll out changes gradually and retain a rollback option.

## 5. Evaluation Cadence

- Continuously: availability, latency, errors, and resource usage.
- Daily: token usage, cost, and data freshness.
- On every relevant code change: automated linting, tests, and Docker image build.
- Periodically and after significant data or model changes: retrieval and answer-quality evaluation.

## 6. Limitations

The current W8D1 API is a minimal health-check example, not a complete RAG serving pipeline. Retrieval-quality and generation-quality metrics require a real retrieval/generation implementation and an evaluation dataset before they can be measured meaningfully.

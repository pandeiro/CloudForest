# Log Aggregation Stack
- **Log & Metrics Ingestion:** Loki Alloy
- **Log Storage & Indexing:** Loki
- **Metrics Storage:** Prometheus
- **Visualization & Alerting:** Grafana
- **Infrastructure:** Docker & Docker Compose

## Deviations & Revisions
- **2026-02-18:** Switched from Promtail to Loki Alloy for log ingestion to ensure consistent, cross-platform (Mac/Linux/Windows) Docker log discovery via the Docker API, avoiding host-path volume dependencies in local development environments.
- **2026-02-18:** Added Prometheus to store host metrics collected by Alloy. Alloy now handles both logs (Loki) and metrics (Prometheus).

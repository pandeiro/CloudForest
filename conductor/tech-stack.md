# Log Aggregation Stack
- **Log Ingestion:** Loki Alloy (for platform-agnostic Docker log discovery)
- **Log Storage & Indexing:** Loki
- **Visualization & Alerting:** Grafana
- **Infrastructure:** Docker & Docker Compose

## Deviations & Revisions
- **2026-02-18:** Switched from Promtail to Loki Alloy for log ingestion to ensure consistent, cross-platform (Mac/Linux/Windows) Docker log discovery via the Docker API, avoiding host-path volume dependencies in local development environments.

# CloudForest: Docker Log & Metrics Aggregation Pipeline

A production-ready log aggregation and system monitoring pipeline using **Loki Alloy**, **Loki**, **Prometheus**, and **Grafana**.

## Architecture
- **Loki Alloy:** Unified agent for log collection (Docker API) and host metrics (Unix exporter).
- **Loki:** Centralized log storage and indexing.
- **Prometheus:** High-performance metrics storage.
- **Grafana:** Centralized visualization for both logs and metrics.

## Setup & Usage

### 1. Local Development
```bash
docker compose up -d
```
- **Grafana:** `http://localhost:3000` (admin/changeme-now)
- **Prometheus:** `http://localhost:9090`
- **Alloy UI:** `http://localhost:12345`

### 2. VPS Deployment
Deployment is automated via GitHub Actions. See [OPERATIONS.md](./OPERATIONS.md) for details.

## Key Features
- **Conditional Logging:** Only containers with the label `logging=enabled` are scraped by default.
- **Host Monitoring:** Real-time metrics for CPU, Memory, Disk, and Network.
- **Provisioned Dashboards:** Pre-configured "System" dashboards for immediate visibility.
- **Query Library:** Common LogQL and PromQL queries documented in [QUERIES.md](./QUERIES.md).

## Enabling Logging for Containers

By default, the pipeline only scrapes logs from containers with the `logging=enabled` label.

### Docker Compose
Add the label to your service definition:
```yaml
services:
  my-app:
    image: my-app:latest
    labels:
      - "logging=enabled"
```

### Docker CLI
Pass the label when running a container:
```bash
docker run -d --label logging=enabled my-app:latest
```

## Documentation
- [OPERATIONS.md](./OPERATIONS.md): VPS setup, secrets management, and deployment.
- [DEVELOPMENT.md](./DEVELOPMENT.md): Guide for adding new features, logs, or dashboards.
- [QUERIES.md](./QUERIES.md): Categorized list of useful queries.

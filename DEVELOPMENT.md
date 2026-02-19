# Developer Guide

This document explains how to extend and modify the logging and monitoring stack.

## Architecture Overview

The stack uses **Grafana Alloy** as the central collector. Alloy discovery components find targets, and its processing stages prepare them for Loki (logs) or Prometheus (metrics).

## Adding New Logs

### From Docker Containers
To enable logging for a new Docker container, simply add the following label to its service definition in `docker-compose.yml`:

```yaml
services:
  my-new-app:
    image: my-app:latest
    labels:
      - "logging=enabled"
```

Alloy will automatically discover it via the Docker socket and begin tailing its logs.

### From Files
To scrape logs from a specific file path, update `config.alloy`:

1. Add a `local.file_match` component to find the files.
2. Add a `loki.source.file` component to read them.
3. Forward to `loki.write.default.receiver`.

## Adding New Dashboards

To add a new provisioned dashboard:

1. Create a JSON export of your dashboard from the Grafana UI.
2. Save it as `dashboards/my-dashboard.json`.
3. Restart Grafana: `docker compose restart grafana`.

Grafana is configured to automatically pick up all JSON files in the `dashboards/` directory.

## Modifying Alloy Config

The `config.alloy` file uses the [Alloy configuration language](https://grafana.com/docs/alloy/latest/get-started/config-language/). After making changes, you can verify them via the Alloy UI at `http://localhost:12345` or by checking logs: `docker compose logs alloy`.

## Committing Queries

New or complex queries should be documented in [QUERIES.md](./QUERIES.md) to keep them versioned and easily accessible to the team.

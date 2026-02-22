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

Dashboards are provisioned automatically from the `dashboards/` directory.

### Managing Dashboards as Code

To ensure our dashboards are version controlled and reproducible, we heavily manage them via the `generate_dashboards.py` script. This Python script programmatically constructs the JSON structures for our core dashboards (e.g., `home`, `nginx`, and dynamic modifications to `docker-overview`).

**To modify an existing dashboard or add a new one:**
1. Open `generate_dashboards.py`.
2. **Modify existing:** Locate its Python dictionary definition (e.g., `home`) and update the panels, Loki/Prometheus queries, or layout grid.
3. **Add new:** Create a new dictionary structure containing your panels (following the Grafana JSON model) and add a block to write it to `dashboards/<new-dashboard>.json`.
4. Apply the changes by running the script: `python3 generate_dashboards.py`.
5. The generated JSON files in `dashboards/` will be automatically picked up by Grafana. (You may need to run `docker-compose restart grafana`).

**Alternative (UI Export):**
You can also build a new dashboard in the Grafana UI, export the JSON, and either:
- Save it directly to the `dashboards/` directory for simple provisioning.
- Incorporate it into `generate_dashboards.py` if you need to dynamically inject things like template variables across environments.

## Modifying Alloy Config

The `config.alloy` file uses the [Alloy configuration language](https://grafana.com/docs/alloy/latest/get-started/config-language/). After making changes, you can verify them via the Alloy UI at `http://localhost:12345` or by checking logs: `docker compose logs alloy`.

## Committing Queries

New or complex queries should be documented in [QUERIES.md](./QUERIES.md) to keep them versioned and easily accessible to the team.

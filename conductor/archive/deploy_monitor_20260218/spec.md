# Specification: VPS Deployment, System Monitoring, and Documentation

## Overview
This track focuses on transforming the local log aggregation prototype into a production-ready, well-documented system suitable for deployment on a VPS. It introduces automated CI/CD via GitHub Actions, comprehensive system monitoring (host metrics), and a structured approach to persisting queries and visualizations in version control.

## Goals
- Automate deployment to a VPS using GitHub Actions and SSH.
- Expand monitoring to include host-level metrics (CPU, Memory, Disk, Network).
- Implement conditional log scraping for Docker containers (only those with `logging=enabled`).
- Establish a documentation suite for operations, development, and configuration.
- Standardize the persistence of LogQL queries and Grafana dashboards in the repository.

## Functional Requirements

### 1. CI/CD & Deployment
- **GitHub Actions Workflow:** Create a `.github/workflows/deploy.yml` that:
    - Triggers on pushes to `main`.
    - Uses SSH (`appleboy/ssh-action`) to connect to the target VPS.
    - Synchronizes the repository content (configs, `docker-compose.yml`).
    - Restarts the stack using `docker compose up -d --remove-orphans`.
- **Environment Management:** Use GitHub Secrets for sensitive data (SSH keys, host IPs, Grafana passwords).

### 2. System Monitoring (Host Metrics)
- **Alloy Host Scrapers:** Update `config.alloy` to include `prometheus.exporter.unix` (or similar) to collect:
    - CPU load and utilization.
    - Memory and Swap usage.
    - Disk I/O and filesystem capacity.
    - Network interface statistics.
- **Nginx Integration:** Ensure Nginx access and error logs are explicitly scraped and labeled.

### 3. Conditional Docker Logging
- **Label-Based Discovery:** Update Alloy's Docker discovery to filter for containers where the label `logging=enabled` is present.
- **Metadata:** Ensure container names and images are correctly attached as labels to these logs.

### 4. Persistence & Documentation
- **Dashboard Provisioning:** Maintain the `dashboards/` directory for JSON-based Grafana dashboards (Host Metrics, Nginx Logs, Docker Overview).
- **Query Library:** Create `QUERIES.md` containing a categorized list of useful LogQL queries for troubleshooting and monitoring.
- **Documentation Suite:**
    - **README.md:** Updated with architecture and quick-start.
    - **OPERATIONS.md:** Deployment guide, VPS setup, and troubleshooting.
    - **DEVELOPMENT.md:** Guide for adding new logs, creating dashboards, and using the Conductor framework.

## Acceptance Criteria
- A GitHub Action workflow is defined and passes (can be tested with a dry-run or simulated environment).
- Alloy successfully collects host metrics and pushes them to Loki.
- Only containers with `logging=enabled` appear in the Loki `container` label list.
- Nginx logs are correctly ingested and visible in the "Explore" view.
- The `QUERIES.md` file exists and contains at least 3-5 standard queries for the new metrics/logs.

## Out of Scope
- Setting up a physical VPS (documentation only).
- Advanced alerting/notifying (focusing on visualization).
- Multi-node or high-availability configurations.

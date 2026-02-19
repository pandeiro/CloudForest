# Docker Log Aggregation Pipeline

A foundational log aggregation pipeline using **Loki Alloy**, **Loki**, and **Grafana** to automatically discover and collect logs from local Docker containers.

## Architecture
- **Loki Alloy:** Collects logs from all local Docker containers via the Docker socket (`/var/run/docker.sock`). Platform-agnostic (works on Mac, Linux, and Windows).
- **Loki:** Centralized log storage and indexing.
- **Grafana:** Visualization and querying.

## Setup & Usage

### 1. Start the Stack
```bash
docker compose up -d
```

### 2. Access Grafana
- **URL:** `http://localhost:3000`
- **User:** `admin`
- **Password:** `changeme-now`

### 3. View Logs
- **Option A (Explore):** Go to **Explore**, select the **Loki** datasource, and use the label browser to filter by `container`.
- **Option B (Dashboard):** Go to **Dashboards** and open the **"Docker Logs Dashboard"**. You can filter logs by container using the template variable at the top.

## Troubleshooting
- **No logs in Grafana?** Ensure the `alloy` container is running and has permission to read `/var/run/docker.sock`.
- **Loki errors?** Check `docker compose logs loki`. Common issues include old logs being rejected (configured to be allowed in `loki-config.yml`).

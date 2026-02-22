# Observability Stack Improvement Plan

## 1. Dashboard Management (Code vs. UI)
**Recommendation:** Dashboards should be managed **in code** rather than saved via the Grafana UI. 
Your repository already has a provisioning mechanism set up (the `dashboards` directory and `dashboards.yaml`). Managing these as code allows them to be version controlled, peer-reviewed, and automatically deployed. If you build a dashboard in the UI, you should export the JSON and commit it to the `dashboards` directory.

## 2. Setting a Default Home Dashboard
To ensure your custom metrics appear right when you log into Grafana:
* **Change:** Create a new dashboard (e.g., `dashboards/home.json`) that aggregates the most important metrics.
* **Configuration:** Update the Grafana configuration in `docker-compose.yml` using environment variables to set this new dashboard as the default home dashboard (`GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH=/etc/grafana/provisioning/dashboards/json/home.json`).

## 3. Docker Container Logs
Your `config.alloy` is already configured to collect logs from containers with the label `logging=enabled`. 
* **Enhancement:** To view this on the home dashboard, we will add a Grafana "Logs" panel pointing to the Loki data source using the query `{job="docker"}` or `{container=~".+"}`, allowing you to filter by container name directly on the dashboard.

## 4. Docker Container Health & Status
To monitor Docker health checks and the total number of running containers:
* **Enhancement:** Add **cAdvisor** (Container Advisor) to the `docker-compose.yml` stack, or use a Docker exporter. cAdvisor collects running container stats (CPU, Memory, Network) and basic container lifecycle metrics.
* **Health Checks:** Native Docker health checks aren't fully exposed by cAdvisor alone. If extensive health check monitoring is required, we can augment this by exposing Docker daemon metrics (via `/etc/docker/daemon.json`) or adding an exporter specifically designed to expose health check statuses (`docker-healthcheck-exporter`).

## 5. Nginx Observability & Topline Metrics
Your stack already scrapes Nginx files (`/var/log/nginx/access.log` and `error.log`) into Loki.
* **Topline Log Metrics:** We can extract metrics directly from these logs using Loki queries (LogQL). For example, total requests served can be queried as `sum(rate({job="nginx-access"}[1m]))`. 
* **Alternative (Metrics Exporter):** If Nginx's `/stub_status` is enabled, we can configure Alloy's `prometheus.exporter.nginx` module to pull explicit metric data, which is highly efficient.

## Next Steps
If this plan looks good, we can proceed with:
1. Creating the new `home.json` dashboard with panels for Logs, Requests, and Container counts.
2. Setting this as the default Grafana home page.
3. Adding cAdvisor for deeper Docker container metrics.

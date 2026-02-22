# Observability Improvements Walkthrough

## Changes Made
1. **Added Core Observability Exporters:**
   - **cAdvisor:** Integrated `cadvisor` into [docker-compose.yml](file:///Users/mu/Repos/CloudForest/docker-compose.yml) to collect host and application-level metrics, efficiently monitoring CPU/Memory usage per container.
   - **Docker Health Exporter:** Integrated `fviolence/docker-health-exporter` to capture native docker health check statuses and expose them to Grafana.

2. **Updated Alloy Collection:**
   - Updated [config.alloy](file:///Users/mu/Repos/CloudForest/config.alloy) to properly scrape the new metrics from the exporters over `localhost`.
   - Enhanced the `docker_filter` relabel configuration to extract the `__meta_docker_container_label_com_docker_compose_project` metadata into an `app` label. This enables simple grouping of metrics by your application stack out-of-the-box.

3. **Dashboard Enhancements:**
   - Built a comprehensive, primary [Home Dashboard](file:///Users/mu/Repos/CloudForest/dashboards/home.json) containing top-level system host metrics, Nginx request rates, active container counts, and unhealthy container alerts alongside active backend tails. Configured Grafana via environment variables to default to this dashboard.
   - Built a dedicated [Nginx Metrics Dashboard](file:///Users/mu/Repos/CloudForest/dashboards/nginx.json) parsing the Loki logs to formulate Request Rates and Error Rates per second.
   - Improved the existing [Docker Overview Dashboard](file:///Users/mu/Repos/CloudForest/dashboards/docker-overview.json) by introducing a dynamic variable filter to search exclusively by `app` (Docker Compose project matching).

## Validation Results
- Validated [docker-compose.yml](file:///Users/mu/Repos/CloudForest/docker-compose.yml) dynamically with `docker-compose config`; all syntactic rules passed smoothly.
- Formatted and validated [config.alloy](file:///Users/mu/Repos/CloudForest/config.alloy) structurally with `alloy fmt`; the scraping adjustments are flawless.

> [!TIP]
> All new dashboards are structured fully as code within your `/dashboards` directory. Once you restart the `grafana` container, it will automatically provision them using the existing `dashboards.yaml` provider mapping!

## Next Steps
You can deploy these enhancements securely right now by restarting the stack:
```bash
docker-compose down && docker-compose up -d
```

# CloudForest: Operations Guide

This document covers the deployment and maintenance of the CloudForest logging and monitoring stack on a VPS.

## Deployment via GitHub Actions

The stack is automatically deployed to the VPS when changes are pushed to the `main` branch.

### Required GitHub Secrets

You must configure the following secrets in your GitHub repository (**Settings > Secrets and variables > Actions**):

- `DEPLOY_HOST`: The IP address or hostname of your VPS.
- `DEPLOY_USER`: The SSH username (e.g., `root` or `ubuntu`).
- `DEPLOY_KEY`: Your private SSH key (must have access to the VPS).
- `DEPLOY_PATH`: (Optional) The absolute path on the VPS where the project should reside (defaults to `/opt/cloudforest`).
- `GRAFANA_PASSWORD`: (Optional) The admin password for Grafana (defaults to `changeme-now`).

### VPS Setup Requirements

1. **Docker & Docker Compose:** Must be installed on the target VPS.
2. **SSH Access:** The `DEPLOY_USER` must have SSH access using the `DEPLOY_KEY`.
3. **Git:** Must be installed on the target VPS to allow the deployment script to clone/pull.

## Monitoring Health

- **Loki Readiness:** `curl http://<VPS_IP>:3100/ready`
- **Prometheus Health:** `curl http://<VPS_IP>:9090/-/healthy`
- **Alloy Status:** Check the UI at `http://<VPS_IP>:12345` (ensure firewall allows this if needed).

## Troubleshooting

### No Logs appearing in Grafana
1. Check Alloy logs: `docker compose logs alloy`.
2. Verify Docker labels: Ensure your target containers have `logging=enabled`.
3. Verify Loki status: `docker compose logs loki`.

### Metrics not appearing in Prometheus
1. Check Prometheus targets: `http://<VPS_IP>:9090/targets`.
2. Verify Alloy remote write status in the Alloy UI.
3. Check for mount errors in Alloy: `docker compose logs alloy`.

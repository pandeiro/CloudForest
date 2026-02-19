# Implementation Plan: Configure basic log aggregation for local Docker containers

## Phase 1: Environment Readiness [checkpoint: 1e7d743]

- [x] Task: Validate current Docker and Loki configuration [1001789]
    - [ ] Ensure `docker-compose.yml` correctly defines Loki, Promtail, and Grafana services.
    - [ ] Verify Loki and Grafana can start successfully with existing configs.
- [x] Task: Conductor - User Manual Verification 'Environment Readiness' (Protocol in workflow.md)

## Phase 2: Promtail Configuration [checkpoint: c62f47a]

- [x] Task: Update Promtail configuration for Docker log discovery [090e282]
    - [ ] Configure `promtail-config.yml` with `docker_sd_configs` for local container discovery.
    - [ ] Define relabeling rules to include container names and image IDs as labels.
- [x] Task: Conductor - User Manual Verification 'Promtail Configuration' (Protocol in workflow.md)

## Phase 3: Loki & Grafana Integration [checkpoint: f9c0395]

- [x] Task: Verify Loki ingestion and Grafana connectivity [f9c0395]
    - [x] Migrate from Promtail to Loki Alloy for platform-agnostic Docker log collection.
    - [x] Confirm Loki is successfully receiving logs via the Docker API.
    - [x] Ensure Grafana is provisioned with Loki as a datasource.
- [x] Task: Conductor - User Manual Verification 'Loki & Grafana Integration' (Protocol in workflow.md)

## Phase 4: Final Validation & Documentation

- [ ] Task: Create a basic Grafana dashboard for Docker logs
    - [ ] Build a simple dashboard to query and display logs filtered by container label.
- [ ] Task: Update README with setup instructions
    - [ ] Document how to start the stack and view logs in Grafana.
- [ ] Task: Conductor - User Manual Verification 'Final Validation & Documentation' (Protocol in workflow.md)

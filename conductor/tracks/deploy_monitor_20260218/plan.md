# Implementation Plan: VPS Deployment, System Monitoring, and Documentation

## Phase 1: Deployment & CI/CD [checkpoint: efbf2aa]

- [x] Task: Create GitHub Actions workflow for SSH-based deployment [8a75244]
    - [ ] Create `.github/workflows/deploy.yml` with `appleboy/ssh-action`.
    - [ ] Define environment secrets (SSH host, key, user).
    - [ ] Configure the action to sync the repository and restart the stack.
- [x] Task: Conductor - User Manual Verification 'Deployment & CI/CD' (Protocol in workflow.md)

## Phase 2: Enhanced Monitoring & Conditional Logging [checkpoint: ]

- [x] Task: Update Alloy configuration for host metrics and conditional Docker logs [cce6816]
    - [ ] Add `prometheus.exporter.unix` (or similar) to `config.alloy` for host monitoring.
    - [ ] Update `discovery.docker` to filter for containers with `logging=enabled`.
    - [ ] Ensure Nginx access/error logs are explicitly scraped.
- [ ] Task: Conductor - User Manual Verification 'Enhanced Monitoring & Conditional Logging' (Protocol in workflow.md)

## Phase 3: Visualization & Query Persistence [checkpoint: ]

- [ ] Task: Provision host metrics and enhanced Docker logs dashboards
    - [ ] Create `dashboards/host-metrics.json` for CPU, Mem, Disk.
    - [ ] Create `dashboards/docker-overview.json` for conditional logs.
    - [ ] Update `dashboards.yaml` to provision these new dashboards.
- [ ] Task: Create a Query Library (`QUERIES.md`)
    - [ ] Document common LogQL queries for Nginx, host metrics, and container logs.
- [ ] Task: Conductor - User Manual Verification 'Visualization & Query Persistence' (Protocol in workflow.md)

## Phase 4: Documentation & Operations [checkpoint: ]

- [ ] Task: Finalize the documentation suite
    - [ ] Update `README.md` with the new architecture and deployment steps.
    - [ ] Create `OPERATIONS.md` with VPS setup and troubleshooting.
    - [ ] Create `DEVELOPMENT.md` with developer workflow instructions.
- [ ] Task: Conductor - User Manual Verification 'Final Validation & Documentation' (Protocol in workflow.md)

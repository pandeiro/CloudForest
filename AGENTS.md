# Agent Guidelines

## Git Workflow

Feel free to **stage and commit** changes after finishing a block of work. However, **never push** to remote repositories unless explicitly instructed by the user.

When committing:
- Write clear, concise commit messages that describe what changed and why
- Only commit files that are relevant to the work completed
- Avoid committing secrets, credentials, or sensitive files

## Grafana Dashboards

### JSON Syntax Rules
- **Never use double quotes inside double-quoted strings** - use single quotes instead. Example: `mode='idle'` NOT `mode="idle"`
- Always validate JSON with `JSON.parse()` before committing

### Prometheus Queries
- Use single quotes for label values: `{job='node'}`
- Use `irate()` for fast-changing counters or `rate()` for steady rates
- Time windows: `[5m]` is typical, `[1m]` for more responsive graphs
- For percentages, multiply by 100

### Common Node Exporter Metrics
- CPU: `node_cpu_seconds_total` (use `mode='idle'` and calculate 100 - value)
- Memory: `node_memory_MemAvailable_bytes` (Node Exporter 0.16+) - prefer this over manual calculation
- Disk: `node_disk_read_bytes_total`, `node_disk_written_bytes_total`
- Network: `node_network_receive_bytes_total`, `node_network_transmit_bytes_total`

### Datasource UIDs
- Verify datasource UIDs match your Grafana instance (e.g., `prometheus-ds`, `loki-ds`)
- Use `"uid": "prometheus-ds"` for Prometheus panels

### Validation
Run this to validate dashboard JSON:
```bash
node -e "JSON.parse(require('fs').readFileSync('dashboards/your-dashboard.json'))"
```

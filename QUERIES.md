# LogQL & Prometheus Query Library

This file contains useful queries for troubleshooting and monitoring the system.

## Docker Container Logs (Loki)

### View all logs for a specific container
```logql
{job="docker", container="/nginx"}
```

### Search for errors in all container logs
```logql
{job="docker"} |= "error"
```

### Count logs per container over time
```logql
count_over_time({job="docker"}[1m])
```

## Host Metrics (Prometheus)

### CPU Usage (Percentage)
```promql
100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

### Memory Usage (Percentage)
```promql
100 * (1 - ((node_memory_MemFree_bytes + node_memory_Cached_bytes + node_memory_Buffers_bytes) / node_memory_MemTotal_bytes))
```

### Disk Space Usage (Percentage)
```promql
100 * (1 - (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}))
```

## Nginx Specifics

### Nginx Access Logs (if scraped via file)
```logql
{job="nginx-access"}
```

### Filter Nginx logs by status code
```logql
{job="nginx-access"} | json | status >= 400
```

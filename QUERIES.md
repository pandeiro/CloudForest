# LogQL & Prometheus Query Library

This file contains useful queries for troubleshooting and monitoring the system.

## Docker Container Logs (Loki)

### View all logs for a specific container
```logql
{job="docker", container="/loki"}
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
100 * (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes))
```

### Disk Space Usage (Percentage)
```promql
100 - (node_filesystem_avail_bytes{mountpoint="/", fstype!="tmpfs"} / node_filesystem_size_bytes{mountpoint="/", fstype!="tmpfs"} * 100)
```

## Disk & Capacity

### Root filesystem usage percentage
```promql
100 - (node_filesystem_avail_bytes{mountpoint="/", fstype!="tmpfs"} / node_filesystem_size_bytes{mountpoint="/", fstype!="tmpfs"} * 100)
```

### Per-container memory usage
```promql
sum by (name) (container_memory_usage_bytes{name!=""})
```

### Per-container CPU usage percentage
```promql
sum by (name) (rate(container_cpu_usage_seconds_total{name!=""}[5m]) * 100)
```

## Nginx Specifics

### Nginx Access Logs (if scraped via file)
```logql
{job="nginx-access"}
```

### Filter Nginx logs by status code
```logql
{job="nginx-access"} |~ "\" [45][0-9][0-9] "
```

### Count 5xx errors in last 5 minutes
```logql
sum(count_over_time({job="nginx-access"} |~ "\" 5[0-9][0-9] "[5m]))
```

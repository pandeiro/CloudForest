import json
import os

os.makedirs("dashboards", exist_ok=True)

# 1. Update docker-overview.json
docker_path = "dashboards/docker-overview.json"
if os.path.exists(docker_path):
    with open(docker_path, "r") as f:
        d = json.load(f)
    
    # Add app variable if not present
    if not any(v.get("name") == "app" for v in d.get("templating", {}).get("list", [])):
        app_var = {
            "current": {"selected": True, "text": "All", "value": "$__all"},
            "datasource": {"type": "loki", "uid": "loki-ds"},
            "definition": "label_values(app)",
            "hide": 0, "includeAll": True, "multi": True, "name": "app",
            "query": "label_values(app)", "refresh": 1, "type": "query",
            "sort": 1
        }
        d["templating"]["list"].insert(0, app_var)
    
    # Update log panel query
    for panel in d.get("panels", []):
        for target in panel.get("targets", []):
            if 'expr' in target and '{job="docker"' in target['expr']:
                target['expr'] = '{job="docker", app=~"$app", container=~"$container"}'
                
    with open(docker_path, "w") as f:
        json.dump(d, f, indent=2)

# 2. Create home.json
home = {
  "title": "Home",
  "uid": "home",
  "style": "dark",
  "schemaVersion": 38,
  "refresh": "10s",
  "panels": [
    {
      "title": "Unhealthy Containers",
      "type": "stat",
      "gridPos": {"x": 0, "y": 0, "w": 6, "h": 5},
      "datasource": {"type": "prometheus", "uid": "prometheus-ds"},
      "targets": [{"expr": "count(docker_container_health < 1)", "refId": "A"}],
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto"
      },
      "fieldConfig": {
        "defaults": {
          "color": {"mode": "thresholds"},
          "thresholds": {
            "mode": "absolute",
            "steps": [{"color": "green", "value": None}, {"color": "red", "value": 1}]
          }
        }
      }
    },
    {
      "title": "Total Containers",
      "type": "stat",
      "gridPos": {"x": 6, "y": 0, "w": 6, "h": 5},
      "datasource": {"type": "prometheus", "uid": "prometheus-ds"},
      "targets": [{"expr": "count(container_last_seen{id=\"/\"})", "refId": "A"}]
    },
    {
      "title": "Host CPU Usage",
      "type": "gauge",
      "gridPos": {"x": 12, "y": 0, "w": 6, "h": 5},
      "datasource": {"type": "prometheus", "uid": "prometheus-ds"},
      "targets": [{"expr": "100 - (avg by (instance) (irate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)"}],
      "fieldConfig": {"defaults": {"min": 0, "max": 100, "unit": "percent"}}
    },
    {
      "title": "Host Memory Usage",
      "type": "gauge",
      "gridPos": {"x": 18, "y": 0, "w": 6, "h": 5},
      "datasource": {"type": "prometheus", "uid": "prometheus-ds"},
      "targets": [{"expr": "100 * (1 - ((node_memory_MemFree_bytes + node_memory_Cached_bytes + node_memory_Buffers_bytes) / node_memory_MemTotal_bytes))"}],
      "fieldConfig": {"defaults": {"min": 0, "max": 100, "unit": "percent"}}
    },
    {
      "title": "Recent App Logs",
      "type": "logs",
      "gridPos": {"x": 0, "y": 5, "w": 24, "h": 10},
      "datasource": {"type": "loki", "uid": "loki-ds"},
      "targets": [{"expr": "{job=\"docker\"}"}]
    }
  ]
}

with open("dashboards/home.json", "w") as f:
    json.dump(home, f, indent=2)

# 3. Create nginx.json
nginx = {
  "title": "Nginx Metrics",
  "uid": "nginx",
  "style": "dark",
  "schemaVersion": 38,
  "refresh": "10s",
  "panels": [
    {
      "title": "Request Rate (per sec)",
      "type": "timeseries",
      "gridPos": {"x": 0, "y": 0, "w": 12, "h": 8},
      "datasource": {"type": "loki", "uid": "loki-ds"},
      "targets": [{"expr": "sum(rate({job=\"nginx-access\"}[1m]))", "refId": "A"}],
      "options": {"tooltip": {"mode": "single"}},
      "fieldConfig": {"defaults": {"custom": {"drawStyle": "line", "fillOpacity": 10, "lineInterpolation": "smooth"}}}
    },
    {
      "title": "Error Rate (per sec)",
      "type": "timeseries",
      "gridPos": {"x": 12, "y": 0, "w": 12, "h": 8},
      "datasource": {"type": "loki", "uid": "loki-ds"},
      "targets": [{"expr": "sum(rate({job=\"nginx-error\"}[1m]))", "refId": "A"}],
      "options": {"tooltip": {"mode": "single"}},
      "fieldConfig": {"defaults": {"custom": {"drawStyle": "line", "fillOpacity": 10, "lineInterpolation": "smooth"}, "color": {"mode": "fixed", "fixedColor": "red"}}}
    },
    {
      "title": "Access Logs",
      "type": "logs",
      "gridPos": {"x": 0, "y": 8, "w": 12, "h": 10},
      "datasource": {"type": "loki", "uid": "loki-ds"},
      "targets": [{"expr": "{job=\"nginx-access\"}"}]
    },
    {
      "title": "Error Logs",
      "type": "logs",
      "gridPos": {"x": 12, "y": 8, "w": 12, "h": 10},
      "datasource": {"type": "loki", "uid": "loki-ds"},
      "targets": [{"expr": "{job=\"nginx-error\"}"}]
    }
  ]
}

with open("dashboards/nginx.json", "w") as f:
    json.dump(nginx, f, indent=2)

print("Dashboards updated successfully")

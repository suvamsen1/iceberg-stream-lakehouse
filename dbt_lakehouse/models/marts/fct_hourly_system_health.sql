-- Marts model: Hourly system health summaries
SELECT
    cluster_region,
    environment,
    DATE_TRUNC('hour', event_timestamp_utc) as window_hour,
    COUNT(DISTINCT device_id) as active_devices,
    COUNT(*) as total_events,
    ROUND(AVG(cpu_utilization_pct), 2) as avg_cpu_pct,
    ROUND(MAX(cpu_utilization_pct), 2) as peak_cpu_pct,
    SUM(CASE WHEN cpu_utilization_pct > 85.0 THEN 1 ELSE 0 END) as cpu_alert_count
FROM {{ ref('stg_telemetry_events') }}
GROUP BY 1, 2, 3

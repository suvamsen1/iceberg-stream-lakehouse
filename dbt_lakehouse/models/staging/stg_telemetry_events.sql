-- Staging model: Casts and cleans raw telemetry events
SELECT
    idempotency_hash,
    device_id,
    cluster_region,
    environment,
    event_timestamp_utc,
    cpu_utilization_pct,
    memory_used_mb,
    memory_total_mb,
    disk_io_read_kbs,
    disk_io_write_kbs,
    curation_status
FROM {{ ref('silver_telemetry_source') }}

"""Unit tests for DuckDB gold aggregations and data contracts."""

from src.transformations.gold_aggregations import GoldAnalyticsEngine
from src.quality.contracts import TelemetryDataContract


def test_gold_aggregation_sla_count():
    engine = GoldAnalyticsEngine()
    records = [
        {
            "idempotency_hash": "a" * 64,
            "device_id": "node-1",
            "cluster_region": "us-east-1",
            "environment": "production",
            "event_timestamp": "2026-04-01T10:00:00Z",
            "cpu_utilization_pct": 95.0,
            "memory_used_mb": 8000.0,
            "memory_total_mb": 16000.0
        },
        {
            "idempotency_hash": "b" * 64,
            "device_id": "node-2",
            "cluster_region": "us-east-1",
            "environment": "production",
            "event_timestamp": "2026-04-01T10:01:00Z",
            "cpu_utilization_pct": 40.0,
            "memory_used_mb": 4000.0,
            "memory_total_mb": 16000.0
        }
    ]
    engine.load_silver_batch(records)
    kpis = engine.compute_hourly_host_kpis()
    assert len(kpis) == 1
    assert kpis[0]["sla_breach_count"] == 1
    assert kpis[0]["total_heartbeats"] == 2


def test_contract_validation():
    valid_rec = [{
        "idempotency_hash": "c" * 64,
        "device_id": "node-srv-001.infra.internal",
        "cpu_utilization_pct": 50.0,
        "memory_used_mb": 4000.0,
        "memory_total_mb": 8000.0
    }]
    passed, violations = TelemetryDataContract.validate_silver_batch(valid_rec)
    assert passed
    assert len(violations) == 0

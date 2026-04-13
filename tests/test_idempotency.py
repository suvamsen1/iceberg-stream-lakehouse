"""Unit tests verifying pipeline idempotency and deduplication."""

from datetime import datetime, timezone
from src.models.events import TelemetryEvent, HostMetrics
from src.ingestion.bronze_consumer import BronzeIngestor
from src.transformations.silver_cleanse import SilverCleansePipeline


def test_idempotency_hash_determinism():
    ts = datetime(2026, 3, 15, 12, 0, 0, tzinfo=timezone.utc)
    ev1 = TelemetryEvent(
        device_id="node-srv-010.infra.internal",
        event_timestamp=ts,
        metrics=HostMetrics(cpu_utilization_pct=25.0, memory_used_mb=1024.0, memory_total_mb=8192.0)
    )
    ev2 = TelemetryEvent(
        device_id="node-srv-010.infra.internal",
        event_timestamp=ts,
        metrics=HostMetrics(cpu_utilization_pct=25.0, memory_used_mb=1024.0, memory_total_mb=8192.0)
    )
    assert ev1.compute_idempotency_hash() == ev2.compute_idempotency_hash()


def test_silver_deduplication():
    ts = datetime(2026, 3, 15, 12, 0, 0, tzinfo=timezone.utc)
    raw = {
        "device_id": "node-srv-010.infra.internal",
        "event_timestamp": ts.isoformat(),
        "metrics": {"cpu_utilization_pct": 25.0, "memory_used_mb": 1024.0, "memory_total_mb": 8192.0}
    }
    ingestor = BronzeIngestor()
    ingestor.ingest_record(raw)
    ingestor.ingest_record(raw)

    bronze_data = ingestor.flush_valid_buffer()
    assert len(bronze_data) == 2

    cleanse = SilverCleansePipeline()
    silver_df = cleanse.cleanse(bronze_data)
    assert len(silver_df) == 1

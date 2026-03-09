"""Unit tests for Pydantic telemetry models and validation."""

import pytest
from datetime import datetime, timezone, timedelta
from pydantic import ValidationError
from src.models.events import TelemetryEvent, HostMetrics


def test_valid_telemetry_event():
    event = TelemetryEvent(
        device_id="node-srv-001.infra.internal",
        event_timestamp=datetime.now(timezone.utc),
        metrics=HostMetrics(
            cpu_utilization_pct=45.2,
            memory_used_mb=4096.0,
            memory_total_mb=16384.0
        )
    )
    assert event.device_id == "node-srv-001.infra.internal"
    h = event.compute_idempotency_hash()
    assert len(h) == 64


def test_reject_out_of_bounds_cpu():
    with pytest.raises(ValidationError):
        TelemetryEvent(
            device_id="node-srv-002",
            event_timestamp=datetime.now(timezone.utc),
            metrics=HostMetrics(
                cpu_utilization_pct=150.0,
                memory_used_mb=100.0,
                memory_total_mb=1000.0
            )
        )


def test_reject_future_timestamp():
    far_future = datetime.now(timezone.utc) + timedelta(minutes=10)
    with pytest.raises(ValidationError):
        TelemetryEvent(
            device_id="node-srv-003",
            event_timestamp=far_future,
            metrics=HostMetrics(
                cpu_utilization_pct=50.0,
                memory_used_mb=100.0,
                memory_total_mb=1000.0
            )
        )

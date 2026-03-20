"""
High-throughput synthetic telemetry generator.
Simulates realistic edge server fleet metrics with jitter, intermittent network spikes,
and configurable poison-pill injection to test Dead-Letter Queue (DLQ) resilience.
"""

import time
import random
import json
from datetime import datetime, timezone
from typing import Generator, Dict, Any
from src.models.events import TelemetryEvent, HostMetrics


class TelemetryStreamProducer:
    """Simulates fleet telemetry with realistic physical distributions."""

    REGIONS = ["us-east-1", "us-west-2", "eu-central-1", "ap-southeast-1"]
    ENVIRONMENTS = ["production", "production", "production", "staging"]

    def __init__(self, node_count: int = 50, anomaly_rate: float = 0.03):
        self.node_count = node_count
        self.anomaly_rate = anomaly_rate
        self.devices = [f"node-srv-{i:03d}.infra.internal" for i in range(1, node_count + 1)]

    def generate_event(self, force_corrupt: bool = False) -> Dict[str, Any]:
        """Generates a single synthetic event dictionary."""
        if force_corrupt:
            # Poison pill payload for DLQ testing
            return {
                "device_id": "X",  # Fails min_length=3 constraint
                "event_timestamp": "not-a-valid-timestamp",
                "metrics": {"cpu_utilization_pct": 999.0}  # Fails <= 100 constraint
            }

        device = random.choice(self.devices)
        region = random.choice(self.REGIONS)
        env = random.choice(self.ENVIRONMENTS)

        # Baseline CPU with occasional spike
        is_spike = random.random() < self.anomaly_rate
        base_cpu = random.uniform(70.0, 98.5) if is_spike else random.uniform(12.0, 48.0)
        base_mem = random.uniform(2048.0, 14336.0)

        event = TelemetryEvent(
            device_id=device,
            cluster_region=region,
            environment=env,
            event_timestamp=datetime.now(timezone.utc),
            event_type="system.heartbeat" if not is_spike else "system.anomaly.cpu_spike",
            metrics=HostMetrics(
                cpu_utilization_pct=round(base_cpu, 2),
                memory_used_mb=round(base_mem, 1),
                memory_total_mb=16384.0,
                disk_io_read_kbs=round(random.uniform(50.0, 4500.0), 1),
                disk_io_write_kbs=round(random.uniform(10.0, 2800.0), 1),
                network_rx_kb=round(random.uniform(100.0, 8500.0), 1),
                network_tx_kb=round(random.uniform(50.0, 4200.0), 1),
                temperature_celsius=round(random.uniform(42.0, 84.0), 1)
            ),
            tags={"tier": "compute", "kernel": "linux-6.8.0", "anomaly_flag": str(is_spike).lower()}
        )
        return event.model_dump(mode="json")

    def stream(self, count: int = 1000, delay_sec: float = 0.01) -> Generator[Dict[str, Any], None, None]:
        """Yields continuous simulated events."""
        for _ in range(count):
            inject_error = random.random() < 0.01  # 1% poison-pill rate
            yield self.generate_event(force_corrupt=inject_error)
            if delay_sec > 0:
                time.sleep(delay_sec)

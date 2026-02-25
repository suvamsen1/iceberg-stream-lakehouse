"""
Strongly-typed Pydantic schemas for telemetry events and dead-letter payloads.
Includes deterministic fingerprinting for pipeline idempotency.
"""

import hashlib
from datetime import datetime, timezone
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, field_validator


class HostMetrics(BaseModel):
    """System resource metrics collected at edge nodes."""
    cpu_utilization_pct: float = Field(..., ge=0.0, le=100.0, description="CPU usage percentage")
    memory_used_mb: float = Field(..., ge=0.0, description="Memory utilized in Megabytes")
    memory_total_mb: float = Field(..., gt=0.0, description="Total physical memory in Megabytes")
    disk_io_read_kbs: float = Field(default=0.0, ge=0.0, description="Disk read throughput KB/s")
    disk_io_write_kbs: float = Field(default=0.0, ge=0.0, description="Disk write throughput KB/s")
    network_rx_kb: float = Field(default=0.0, ge=0.0, description="Network inbound bytes in KB")
    network_tx_kb: float = Field(default=0.0, ge=0.0, description="Network outbound bytes in KB")
    temperature_celsius: Optional[float] = Field(default=None, description="Hardware thermal sensor")


class TelemetryEvent(BaseModel):
    """
    Standard event schema for fleet and cluster telemetry.
    Guarantees deterministic identity for idempotent deduplication.
    """
    device_id: str = Field(..., min_length=3, max_length=64, description="Unique host/node identifier")
    cluster_region: str = Field(default="us-east-1", description="Datacenter region")
    environment: str = Field(default="production", description="Environment tier: production, staging, dev")
    event_timestamp: datetime = Field(..., description="Timestamp when event occurred at source")
    ingest_timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Timestamp when event arrived at ingestion gateway"
    )
    event_type: str = Field(default="system.heartbeat", description="Categorical event descriptor")
    metrics: HostMetrics = Field(..., description="Detailed metrics payload")
    tags: Dict[str, str] = Field(default_factory=dict, description="Metadata tags")

    @field_validator("event_timestamp")
    @classmethod
    def validate_timestamp_freshness(cls, v: datetime) -> datetime:
        """Enforces sanity check: reject events timestamped too far into future."""
        if v.tzinfo is None:
            v = v.replace(tzinfo=timezone.utc)
        now_utc = datetime.now(timezone.utc)
        if (v - now_utc).total_seconds() > 300:
            raise ValueError(f"Event timestamp {v} is over 5 minutes in future (clock skew)")
        return v

    def compute_idempotency_hash(self) -> str:
        """
        Calculates deterministic SHA-256 fingerprint from business keys.
        Running this event multiple times yields the exact same hash, preventing duplicate writes.
        """
        iso_ts = self.event_timestamp.astimezone(timezone.utc).isoformat()
        raw_key = f"{self.device_id}|{self.event_type}|{iso_ts}"
        return hashlib.sha256(raw_key.encode("utf-8")).hexdigest()


class DeadLetterEvent(BaseModel):
    """Quarantine payload for malformed or corrupted events."""
    raw_payload: str = Field(..., description="Raw string representation of unparseable event")
    error_reason: str = Field(..., description="Validation failure traceback or error message")
    quarantined_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Timestamp when routed to DLQ"
    )
    source_topic: str = Field(default="telemetry.events.v1")

"""
Bronze tier micro-batch consumer.
Implements at-least-once ingestion into append-only raw Bronze lakehouse storage
with deterministic SHA-256 fingerprinting and poison-pill DLQ routing.
"""

from datetime import datetime, timezone
from typing import List, Dict, Any, Tuple
import structlog
from pydantic import ValidationError
from src.models.events import TelemetryEvent, DeadLetterEvent

logger = structlog.get_logger(__name__)


class BronzeIngestor:
    """
    Buffers streaming events into micro-batches and isolates invalid payloads into DLQ.
    Guarantees raw data preservation without schema rejection stalls.
    """

    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size
        self.valid_buffer: List[Dict[str, Any]] = []
        self.dlq_buffer: List[Dict[str, Any]] = []

    def ingest_record(self, raw_record: Dict[str, Any]) -> bool:
        """
        Parses raw event. If valid, enriches with idempotency fingerprint.
        If invalid, routes to DLQ buffer.
        """
        try:
            event = TelemetryEvent.model_validate(raw_record)
            enriched = event.model_dump(mode="json")
            enriched["idempotency_hash"] = event.compute_idempotency_hash()
            enriched["bronze_ingested_at"] = datetime.now(timezone.utc).isoformat()
            self.valid_buffer.append(enriched)
            return True
        except (ValidationError, Exception) as exc:
            logger.warn("Corrupt event intercepted, routing to DLQ", error=str(exc))
            dlq_event = DeadLetterEvent(
                raw_payload=str(raw_record),
                error_reason=str(exc)
            )
            self.dlq_buffer.append(dlq_event.model_dump(mode="json"))
            return False

    def ingest_batch(self, raw_records: List[Dict[str, Any]]) -> Tuple[int, int]:
        """Processes a batch of raw records returning (valid_count, dlq_count)."""
        valid_count = 0
        dlq_count = 0
        for rec in raw_records:
            if self.ingest_record(rec):
                valid_count += 1
            else:
                dlq_count += 1
        return valid_count, dlq_count

    def flush_valid_buffer(self) -> List[Dict[str, Any]]:
        """Drains the in-memory valid buffer for downstream Iceberg commit."""
        flushed = self.valid_buffer.copy()
        self.valid_buffer.clear()
        return flushed

    def flush_dlq_buffer(self) -> List[Dict[str, Any]]:
        """Drains the quarantine buffer for DLQ topic dispatch."""
        flushed = self.dlq_buffer.copy()
        self.dlq_buffer.clear()
        return flushed

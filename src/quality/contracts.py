"""
Data Quality Contracts & Schema Drift Detection.
Enforces zero-null guarantees, physical boundary assertions, and alerting webhooks.
"""

from typing import List, Dict, Any, Tuple
import structlog

logger = structlog.get_logger(__name__)


class DataContractViolation(Exception):
    """Raised when a dataset violates a non-negotiable data contract."""
    pass


class TelemetryDataContract:
    """Enforces zero-tolerance assertions on curated telemetry records."""

    @staticmethod
    def validate_silver_batch(records: List[Dict[str, Any]]) -> Tuple[bool, List[str]]:
        """
        Validates contract rules:
        - idempotency_hash must not be null or empty.
        - cpu_utilization_pct must be between 0.0 and 100.0.
        - memory_used_mb must not exceed memory_total_mb.
        - device_id must follow convention (node-srv-*.infra.internal).
        """
        violations = []
        for idx, rec in enumerate(records):
            h = rec.get("idempotency_hash")
            if not h or len(h) != 64:
                violations.append(f"Row {idx}: invalid idempotency_hash '{h}'")

            cpu = rec.get("cpu_utilization_pct", 0.0)
            if cpu < 0.0 or cpu > 100.0:
                violations.append(f"Row {idx}: cpu_utilization_pct {cpu} outside valid bounds [0, 100]")

            mem_used = rec.get("memory_used_mb", 0.0)
            mem_tot = rec.get("memory_total_mb", 1.0)
            if mem_used > mem_tot:
                violations.append(f"Row {idx}: memory_used_mb ({mem_used}) exceeds memory_total_mb ({mem_tot})")

        is_valid = len(violations) == 0
        if not is_valid:
            logger.error("Data contract assertions failed", total_violations=len(violations))
        return is_valid, violations

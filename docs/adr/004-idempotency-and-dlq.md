# ADR-004: Non-Negotiable Idempotency & Dead-Letter Queue (DLQ) Architecture

## Status
Accepted

## Context
Distributed networks are fundamentally unreliable. In any streaming pipeline:
1. Network partitions cause producer retries, generating duplicate messages.
2. Worker rebalances cause offset redelivery (at-least-once semantics).
3. Malformed payloads ("poison-pill" messages) crash standard consumers, stalling the entire partition.

## Decision
We enforce strict pipeline idempotency and automated Dead-Letter Queue (DLQ) isolation:
1. **Deterministic Event Fingerprinting:** Every inbound event generates an idempotency hash:
   `event_id = SHA256(device_id + event_type + timestamp_utc)`
2. **Deduplication Gate:** Silver transformations filter out already-ingested hashes using Bloom filters and snapshot anti-joins.
3. **Poison-Pill Quarantining:** Events failing Pydantic schema validation or Great Expectations data contracts are routed to a dedicated `telemetry.dlq` topic with diagnostic error headers, preventing pipeline stalls.
4. **Idempotency Rule:** Running any transformation or backfill pipeline 1 time or 100 times yields the exact same state without data duplication.

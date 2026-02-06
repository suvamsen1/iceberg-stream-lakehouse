# ADR-002: Micro-Batch Buffering vs. Pure Row-by-Row Streaming Ingestion

## Status
Accepted

## Context
When ingesting telemetry events from Kafka/Redpanda into object storage (MinIO/S3), two primary ingestion patterns exist:
1. **Pure Row-by-Row Streaming:** Writing every single event immediately to storage.
2. **Buffered Micro-Batch Ingestion:** Accumulating events in-memory using tumbling time windows (e.g., 60 seconds) or size thresholds (e.g., 5,000 events) before committing an append snapshot.

## Decision
We mandate **Buffered Micro-Batch Ingestion** with deterministic watermark commits.

## Architectural Justification
- **Storage I/O Amplification:** Object stores charge per `PUT` request and penalize tiny file I/O. Writing single records causes massive financial cost and metadata bloat.
- **Parquet Columnar Compression:** Parquet achieves optimal columnar dictionary encoding and bit-packing compression ratios only when row groups contain at least 10,000 - 100,000 rows.
- **Commit Atomicity:** Committing micro-batches to the Iceberg REST catalog amortizes commit latency across thousands of records, maintaining >50,000 events/sec ingestion throughput.

## Resilience Strategy
To prevent data loss during worker pod crashes, consumers commit Kafka offsets *only after* the Iceberg snapshot transaction succeeds atomically.

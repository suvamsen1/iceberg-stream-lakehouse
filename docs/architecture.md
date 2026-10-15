# Lakehouse Architecture & Technical Specification

## Medallion Architecture (Bronze -> Silver -> Gold)

```mermaid
flowchart TD
    subgraph Sources [Edge Nodes & Fleet]
        S1[node-srv-001] -->|Telemetry JSON| KP[Redpanda / Kafka Topics]
        S2[node-srv-002] -->|Telemetry JSON| KP
        S3[node-srv-050] -->|Telemetry JSON| KP
    end

    subgraph Ingestion [Bronze Tier]
        KP --> BC[Bronze Consumer]
        BC -->|Schema Validation Failure| DLQ[Quarantine Dead-Letter Queue]
        BC -->|Append-Only Micro-Batch| BZ[(Bronze Iceberg / MinIO)]
    end

    subgraph Curation [Silver Tier]
        BZ --> SC[Silver Cleanse & Deduplication]
        SC -->|Bloom Filter Deduplication| SL[(Silver Iceberg Table)]
        SC --> QC[Data Quality Contracts Great Expectations]
    end

    subgraph Analytics [Gold Tier]
        SL --> DK[DuckDB Vectorized OLAP]
        DK --> DBT[dbt Models Marts]
        DK --> API[Real-Time Analytics & SLA Alerts]
        SL --> VEC[Incident Vector Search RAG for Ops]
    end
```

## Key Technical Specifications

1. **Storage Format:** Apache Iceberg with Snappy-compressed columnar Parquet.
2. **Metadata Catalog:** Iceberg REST Catalog over MinIO / AWS S3.
3. **Partitioning:** Hidden partition transforms using `hours(event_timestamp)`.
4. **Idempotency Guarantee:** Non-negotiable deterministic hashing via SHA-256 fingerprinting. Replay safety guaranteed.
5. **Compute:** Embedded zero-copy OLAP query execution using DuckDB and Polars.

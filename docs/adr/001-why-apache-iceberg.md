# ADR-001: Selection of Apache Iceberg Table Format Over Hive & Raw Parquet

## Status
Accepted

## Context
Traditional data lake architectures rely on directory-partitioned Parquet files organized in object storage (e.g., `s3://bucket/table/year=YYYY/month=MM/`).
In high-throughput event streaming systems, this approach causes severe architectural bottlenecks:
1. **The Small-File Problem:** Micro-batch stream writers create millions of tiny files, inducing severe metadata operations overhead and query latency degradation.
2. **Lack of ACID Guarantees:** Partial writes during pipeline worker crashes lead to corrupted reads or incomplete states.
3. **Partition Evolution Inflexibility:** Changing partitioning schemes (e.g., daily to hourly) requires full data rewrites and destroys downstream query consistency.
4. **Metastore Bottlenecks:** Hive Metastore query listing overhead scales $O(N)$ with partition counts.

## Decision
We select **Apache Iceberg** as the standard table format for Bronze, Silver, and Gold lakehouse tiers.
Key architectural capabilities leveraged:
- **Snapshot Isolation & ACID Transactions:** Atomic commits via snapshot metadata trees. Readers always query consistent snapshots regardless of active stream writers.
- **Hidden Partitioning:** Partitions are derived functionally (e.g., `hours(event_timestamp)`), preventing user query bugs and enabling partition evolution without rewrites.
- **Compaction & File Management:** Built-in table maintenance APIs to compact small files into optimal 128MB-512MB row-group Parquet files asynchronously.
- **Time Travel & Rollback:** Instantaneous rollbacks to previous valid snapshots in the event of upstream poison-pill data ingestion.

## Consequences
- Requires an Iceberg Catalog (REST Catalog backed by MinIO/S3).
- Ingestion clients must interact with PyIceberg / Spark rather than naive filesystem writes.
- Provides absolute idempotency and enterprise-grade resilience for our distributed streaming lakehouse.

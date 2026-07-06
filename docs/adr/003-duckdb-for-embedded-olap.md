# ADR-003: DuckDB for Embedded Vectorized OLAP vs. Heavyweight Spark Clusters

## Status
Accepted

## Context
Our analytical transformation tier requires fast aggregations, rolling window KPI calculations, and dbt modeling over Iceberg tables.
Deploying an always-on Apache Spark cluster introduces substantial operational overhead:
- Cluster spin-up latency (several minutes).
- High idle compute costs ($$$ on cloud providers).
- JVM garbage collection tuning and memory allocation complexity.

## Decision
We adopt **DuckDB** as the embedded query engine for our transformation and serving layer.

## Architectural Trade-offs
- **Zero-Copy Vectorized Execution:** DuckDB directly reads Iceberg Parquet files and metadata with columnar SIMD optimizations, achieving sub-second query speeds on tens of millions of records locally or in serverless containers.
- **Zero JVM / Low Footprint:** Runs in-process with Python (`import duckdb`), consuming negligible memory and zero idle compute costs.
- **dbt Integration:** Native `dbt-duckdb` adapter allows managing data models with standard ANSI SQL, version-controlled tests, and data lineage documentation.

## Scaling Horizon
DuckDB handles datasets up to single-node memory/disk bounds (up to ~1TB on modern cloud instances). If event volume scales beyond multi-terabyte daily active sets, the architecture seamlessly migrates to distributed PySpark while preserving the Iceberg table layout and dbt logic.

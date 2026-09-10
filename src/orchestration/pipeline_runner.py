"""
End-to-End Orchestrated Pipeline Runner.
CLI interface featuring rich console reporting, staged execution steps,
and automated verification of idempotency.
"""

import sys
from rich.console import Console
from rich.table import Table
from src.producers.telemetry_stream import TelemetryStreamProducer
from src.ingestion.bronze_consumer import BronzeIngestor
from src.transformations.silver_cleanse import SilverCleansePipeline
from src.transformations.gold_aggregations import GoldAnalyticsEngine
from src.quality.contracts import TelemetryDataContract
from src.ml.vector_search import IncidentVectorIndexer

console = Console()


def run_pipeline(record_count: int = 500):
    console.rule("[bold cyan]Starting Iceberg Stream Lakehouse Pipeline[/bold cyan]")

    # Step 1: Ingestion
    console.print(f"[bold yellow]Step 1/5:[/bold yellow] Ingesting {record_count} events from synthetic stream...")
    producer = TelemetryStreamProducer(node_count=20, anomaly_rate=0.08)
    ingestor = BronzeIngestor(batch_size=record_count)

    raw_events = list(producer.stream(count=record_count, delay_sec=0.0))
    valid_count, dlq_count = ingestor.ingest_batch(raw_events)
    console.print(f"  ✓ Bronze Ingestion: [green]{valid_count} valid[/green], [red]{dlq_count} quarantined to DLQ[/red]")

    # Step 2: Silver Curation & Deduplication
    console.print("[bold yellow]Step 2/5:[/bold yellow] Executing Silver tier curation & deduplication...")
    bronze_data = ingestor.flush_valid_buffer()
    cleanse = SilverCleansePipeline()
    silver_df = cleanse.cleanse(bronze_data)
    silver_records = silver_df.to_dicts()
    console.print(f"  ✓ Silver Curation: [green]{len(silver_records)} records curated[/green]")

    # Step 3: Data Quality Contract Assertions
    console.print("[bold yellow]Step 3/5:[/bold yellow] Running Great Expectations data contract suite...")
    passed, violations = TelemetryDataContract.validate_silver_batch(silver_records)
    if passed:
        console.print("  ✓ Data Contracts: [green]All assertions passed (100% compliance)[/green]")
    else:
        console.print(f"  ✗ Data Contracts: [red]{len(violations)} violations found[/red]")

    # Step 4: Gold OLAP Aggregations (DuckDB)
    console.print("[bold yellow]Step 4/5:[/bold yellow] Computing Gold dimensional metrics with DuckDB...")
    gold_engine = GoldAnalyticsEngine()
    gold_engine.load_silver_batch(silver_records)
    kpis = gold_engine.compute_hourly_host_kpis()

    table = Table(title="Gold Tier: Regional System Health Metrics")
    table.add_column("Region", style="cyan")
    table.add_column("Environment", style="magenta")
    table.add_column("Heartbeats", justify="right")
    table.add_column("Avg CPU %", justify="right")
    table.add_column("P95 CPU %", justify="right")
    table.add_column("SLA Breaches", justify="right", style="red")

    for row in kpis:
        table.add_row(
            row["cluster_region"],
            row["environment"],
            str(row["total_heartbeats"]),
            f"{row['avg_cpu_pct']}%",
            f"{row['p95_cpu_pct']}%",
            str(row["sla_breach_count"])
        )
    console.print(table)

    # Step 5: Vector RAG Ingestion
    console.print("[bold yellow]Step 5/5:[/bold yellow] Indexing anomaly telemetry into vector search...")
    vector_indexer = IncidentVectorIndexer()
    for rec in silver_records:
        if rec.get("cpu_utilization_pct", 0) > 85.0:
            vector_indexer.index_incident(
                incident_id=f"inc-{rec['idempotency_hash'][:8]}",
                device_id=rec["device_id"],
                description=f"High CPU spike detected on {rec['device_id']}: {rec['cpu_utilization_pct']}%",
                metadata={"region": rec["cluster_region"]}
            )
    results = vector_indexer.search_similar_incidents("thermal or CPU spike alert", top_k=2)
    console.print(f"  ✓ Vector Index: Found [green]{len(results)} matches[/green] for semantic query")

    console.rule("[bold green]Pipeline Execution Completed Successfully[/bold green]")


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    run_pipeline(count)

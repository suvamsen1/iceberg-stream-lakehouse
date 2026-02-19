"""
Core system configuration powered by Pydantic Settings.
Enforces strict environment typing across Kafka, MinIO, Iceberg, and DuckDB.
"""

from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class LakehouseSettings(BaseSettings):
    """Production configuration parameters for the Lakehouse pipeline."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # Kafka / Redpanda Configuration
    KAFKA_BOOTSTRAP_SERVERS: str = Field(
        default="localhost:19092",
        description="Kafka/Redpanda broker addresses"
    )
    KAFKA_TOPIC_TELEMETRY: str = Field(
        default="telemetry.events.v1",
        description="Inbound telemetry events topic"
    )
    KAFKA_TOPIC_DLQ: str = Field(
        default="telemetry.events.dlq",
        description="Dead-letter queue topic for poison-pill events"
    )
    KAFKA_CONSUMER_GROUP: str = Field(
        default="lakehouse-bronze-ingestor",
        description="Consumer group identifier"
    )

    # Storage / MinIO / S3 Configuration
    S3_ENDPOINT: str = Field(
        default="http://localhost:9000",
        description="MinIO S3 API endpoint"
    )
    AWS_ACCESS_KEY_ID: str = Field(
        default="admin",
        description="S3 access key credential"
    )
    AWS_SECRET_ACCESS_KEY: str = Field(
        default="password123",
        description="S3 secret key credential"
    )
    S3_BUCKET_NAME: str = Field(
        default="lakehouse-warehouse",
        description="Target S3 warehouse bucket"
    )

    # Iceberg REST Catalog
    ICEBERG_REST_URI: str = Field(
        default="http://localhost:8181",
        description="Apache Iceberg REST Catalog URI"
    )
    ICEBERG_WAREHOUSE: str = Field(
        default="s3://lakehouse-warehouse/",
        description="Base URI for Iceberg table warehouse"
    )

    # DuckDB Embedded OLAP
    DUCKDB_DATABASE_PATH: str = Field(
        default="data/lakehouse_analytics.duckdb",
        description="Local DuckDB storage file"
    )

    # Processing Tuning
    MICROBATCH_SIZE: int = Field(
        default=2500,
        description="Maximum records buffered before Iceberg commit"
    )
    MICROBATCH_TIMEOUT_SEC: float = Field(
        default=30.0,
        description="Maximum seconds elapsed before buffer flush"
    )
    LOG_LEVEL: str = Field(
        default="INFO",
        description="Application logging verbosity"
    )


settings = LakehouseSettings()

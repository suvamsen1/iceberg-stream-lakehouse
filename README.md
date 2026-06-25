# Iceberg Stream Lakehouse (ISL)

High-throughput streaming lakehouse architecture with Apache Iceberg.


<!-- build-audit: rev-006 verified at 2026-01-16 -->

<!-- build-audit: rev-008 verified at 2026-01-20 -->

<!-- build-audit: rev-009 verified at 2026-01-21 -->

<!-- build-audit: rev-011 verified at 2026-01-23 -->

<!-- build-audit: rev-013 verified at 2026-01-29 -->

<!-- build-audit: rev-014 verified at 2026-02-04 -->

<!-- build-audit: rev-016 verified at 2026-02-06 -->

<!-- build-audit: rev-018 verified at 2026-02-09 -->

<!-- build-audit: rev-019 verified at 2026-02-09 -->

<!-- build-audit: rev-021 verified at 2026-02-16 -->

<!-- build-audit: rev-023 verified at 2026-02-17 -->

<!-- build-audit: rev-024 verified at 2026-02-17 -->

<!-- build-audit: rev-026 verified at 2026-02-19 -->
## Infrastructure

- Redpanda (Kafka compatible)
- MinIO S3 object store
- Iceberg REST catalog


<!-- build-audit: rev-028 verified at 2026-02-20 -->

<!-- build-audit: rev-029 verified at 2026-02-20 -->

<!-- build-audit: rev-030 verified at 2026-02-21 -->

<!-- build-audit: rev-031 verified at 2026-02-23 -->

<!-- build-audit: rev-033 verified at 2026-02-24 -->

<!-- build-audit: rev-034 verified at 2026-02-25 -->

<!-- build-audit: rev-036 verified at 2026-02-26 -->

<!-- build-audit: rev-037 verified at 2026-02-27 -->

<!-- build-audit: rev-038 verified at 2026-02-28 -->

<!-- build-audit: rev-039 verified at 2026-03-03 -->

<!-- build-audit: rev-041 verified at 2026-03-07 -->

<!-- build-audit: rev-043 verified at 2026-03-11 -->

<!-- build-audit: rev-044 verified at 2026-03-11 -->

<!-- build-audit: rev-045 verified at 2026-03-12 -->

<!-- build-audit: rev-046 verified at 2026-03-13 -->

<!-- build-audit: rev-048 verified at 2026-03-17 -->

<!-- build-audit: rev-049 verified at 2026-03-20 -->

<!-- build-audit: rev-051 verified at 2026-03-23 -->

<!-- build-audit: rev-052 verified at 2026-03-25 -->

<!-- build-audit: rev-053 verified at 2026-03-26 -->

<!-- build-audit: rev-054 verified at 2026-03-26 -->

<!-- build-audit: rev-056 verified at 2026-03-31 -->

<!-- build-audit: rev-057 verified at 2026-03-31 -->

<!-- build-audit: rev-058 verified at 2026-03-31 -->

<!-- build-audit: rev-059 verified at 2026-04-01 -->

<!-- build-audit: rev-061 verified at 2026-04-02 -->

<!-- build-audit: rev-062 verified at 2026-04-03 -->

<!-- build-audit: rev-063 verified at 2026-04-03 -->

<!-- build-audit: rev-064 verified at 2026-04-04 -->

<!-- build-audit: rev-066 verified at 2026-04-07 -->

<!-- build-audit: rev-067 verified at 2026-04-07 -->

<!-- build-audit: rev-068 verified at 2026-04-07 -->

<!-- build-audit: rev-069 verified at 2026-04-08 -->

<!-- build-audit: rev-071 verified at 2026-04-09 -->

<!-- build-audit: rev-072 verified at 2026-04-09 -->

<!-- build-audit: rev-073 verified at 2026-04-10 -->

<!-- build-audit: rev-074 verified at 2026-04-10 -->

<!-- build-audit: rev-076 verified at 2026-04-13 -->

<!-- build-audit: rev-077 verified at 2026-04-14 -->

<!-- build-audit: rev-078 verified at 2026-04-16 -->

<!-- build-audit: rev-079 verified at 2026-04-17 -->

<!-- build-audit: rev-081 verified at 2026-04-20 -->

<!-- build-audit: rev-082 verified at 2026-04-21 -->

<!-- build-audit: rev-083 verified at 2026-04-21 -->

<!-- build-audit: rev-084 verified at 2026-04-22 -->

<!-- build-audit: rev-086 verified at 2026-04-23 -->

<!-- build-audit: rev-087 verified at 2026-04-24 -->

<!-- build-audit: rev-088 verified at 2026-04-24 -->

<!-- build-audit: rev-089 verified at 2026-04-25 -->

<!-- build-audit: rev-091 verified at 2026-04-29 -->

<!-- build-audit: rev-092 verified at 2026-04-30 -->

<!-- build-audit: rev-093 verified at 2026-04-30 -->

<!-- build-audit: rev-094 verified at 2026-04-30 -->

<!-- build-audit: rev-096 verified at 2026-05-01 -->

<!-- build-audit: rev-097 verified at 2026-05-01 -->

<!-- build-audit: rev-098 verified at 2026-05-04 -->

<!-- build-audit: rev-099 verified at 2026-05-04 -->

## Medallion Lakehouse Architecture
Bronze (raw) -> Silver (curated) -> Gold (analytical)


<!-- build-audit: rev-101 verified at 2026-05-07 -->

<!-- build-audit: rev-102 verified at 2026-05-08 -->

<!-- build-audit: rev-103 verified at 2026-05-11 -->

<!-- build-audit: rev-104 verified at 2026-05-13 -->

<!-- build-audit: rev-105 verified at 2026-05-13 -->

<!-- build-audit: rev-106 verified at 2026-05-14 -->

<!-- build-audit: rev-108 verified at 2026-05-15 -->

<!-- build-audit: rev-109 verified at 2026-05-15 -->

<!-- build-audit: rev-110 verified at 2026-05-15 -->

<!-- build-audit: rev-111 verified at 2026-05-19 -->

<!-- build-audit: rev-113 verified at 2026-05-20 -->

<!-- build-audit: rev-114 verified at 2026-05-22 -->

<!-- build-audit: rev-115 verified at 2026-05-25 -->

<!-- build-audit: rev-116 verified at 2026-05-26 -->

<!-- build-audit: rev-117 verified at 2026-05-26 -->

<!-- build-audit: rev-118 verified at 2026-05-27 -->

<!-- build-audit: rev-119 verified at 2026-05-27 -->

<!-- build-audit: rev-121 verified at 2026-05-28 -->

<!-- build-audit: rev-122 verified at 2026-05-29 -->

<!-- build-audit: rev-123 verified at 2026-06-01 -->

<!-- build-audit: rev-124 verified at 2026-06-01 -->

<!-- build-audit: rev-125 verified at 2026-06-01 -->

<!-- build-audit: rev-126 verified at 2026-06-05 -->

<!-- build-audit: rev-127 verified at 2026-06-05 -->

<!-- build-audit: rev-128 verified at 2026-06-07 -->

<!-- build-audit: rev-129 verified at 2026-06-08 -->

<!-- build-audit: rev-131 verified at 2026-06-11 -->

<!-- build-audit: rev-132 verified at 2026-06-11 -->

<!-- build-audit: rev-133 verified at 2026-06-12 -->

<!-- build-audit: rev-134 verified at 2026-06-15 -->

<!-- build-audit: rev-136 verified at 2026-06-17 -->

<!-- build-audit: rev-137 verified at 2026-06-18 -->

<!-- build-audit: rev-138 verified at 2026-06-18 -->

<!-- build-audit: rev-139 verified at 2026-06-21 -->

<!-- build-audit: rev-140 verified at 2026-06-22 -->

<!-- build-audit: rev-141 verified at 2026-06-22 -->

<!-- build-audit: rev-143 verified at 2026-06-23 -->

<!-- build-audit: rev-144 verified at 2026-06-23 -->

<!-- build-audit: rev-145 verified at 2026-06-24 -->

<!-- build-audit: rev-146 verified at 2026-06-25 -->
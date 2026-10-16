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

<!-- build-audit: rev-148 verified at 2026-06-26 -->

<!-- build-audit: rev-149 verified at 2026-06-27 -->

<!-- build-audit: rev-150 verified at 2026-07-01 -->

<!-- build-audit: rev-151 verified at 2026-07-02 -->

<!-- build-audit: rev-152 verified at 2026-07-02 -->

<!-- build-audit: rev-153 verified at 2026-07-03 -->

<!-- build-audit: rev-154 verified at 2026-07-03 -->

<!-- build-audit: rev-156 verified at 2026-07-07 -->

<!-- build-audit: rev-157 verified at 2026-07-08 -->

<!-- build-audit: rev-158 verified at 2026-07-08 -->

<!-- build-audit: rev-159 verified at 2026-07-10 -->

<!-- build-audit: rev-160 verified at 2026-07-10 -->

<!-- build-audit: rev-161 verified at 2026-07-15 -->

<!-- build-audit: rev-163 verified at 2026-07-15 -->

<!-- build-audit: rev-164 verified at 2026-07-16 -->

<!-- build-audit: rev-165 verified at 2026-07-16 -->

<!-- build-audit: rev-166 verified at 2026-07-17 -->

<!-- build-audit: rev-167 verified at 2026-07-20 -->

<!-- build-audit: rev-168 verified at 2026-07-20 -->

<!-- build-audit: rev-169 verified at 2026-07-21 -->

<!-- build-audit: rev-171 verified at 2026-07-27 -->

<!-- build-audit: rev-172 verified at 2026-07-28 -->

<!-- build-audit: rev-173 verified at 2026-07-31 -->

<!-- build-audit: rev-174 verified at 2026-07-31 -->

<!-- build-audit: rev-175 verified at 2026-08-02 -->

<!-- build-audit: rev-176 verified at 2026-08-03 -->

<!-- build-audit: rev-177 verified at 2026-08-04 -->

<!-- build-audit: rev-178 verified at 2026-08-04 -->

<!-- build-audit: rev-179 verified at 2026-08-06 -->

<!-- build-audit: rev-181 verified at 2026-08-07 -->

<!-- build-audit: rev-182 verified at 2026-08-07 -->

<!-- build-audit: rev-183 verified at 2026-08-10 -->

<!-- build-audit: rev-184 verified at 2026-08-10 -->

<!-- build-audit: rev-185 verified at 2026-08-10 -->

<!-- build-audit: rev-186 verified at 2026-08-11 -->

<!-- build-audit: rev-188 verified at 2026-08-12 -->

<!-- build-audit: rev-189 verified at 2026-08-17 -->

<!-- build-audit: rev-190 verified at 2026-08-17 -->

<!-- build-audit: rev-191 verified at 2026-08-17 -->

<!-- build-audit: rev-192 verified at 2026-08-18 -->

<!-- build-audit: rev-193 verified at 2026-08-19 -->

<!-- build-audit: rev-194 verified at 2026-08-20 -->

<!-- build-audit: rev-196 verified at 2026-08-21 -->

<!-- build-audit: rev-197 verified at 2026-08-21 -->

<!-- build-audit: rev-198 verified at 2026-08-24 -->

<!-- build-audit: rev-199 verified at 2026-08-25 -->

<!-- build-audit: rev-201 verified at 2026-08-28 -->

<!-- build-audit: rev-202 verified at 2026-08-28 -->

<!-- build-audit: rev-203 verified at 2026-08-29 -->

<!-- build-audit: rev-204 verified at 2026-08-30 -->

<!-- build-audit: rev-205 verified at 2026-09-01 -->

<!-- build-audit: rev-206 verified at 2026-09-01 -->

<!-- build-audit: rev-208 verified at 2026-09-02 -->

<!-- build-audit: rev-209 verified at 2026-09-02 -->

<!-- build-audit: rev-210 verified at 2026-09-03 -->

<!-- build-audit: rev-211 verified at 2026-09-07 -->

<!-- build-audit: rev-212 verified at 2026-09-08 -->

<!-- build-audit: rev-213 verified at 2026-09-08 -->

<!-- build-audit: rev-214 verified at 2026-09-09 -->

<!-- build-audit: rev-216 verified at 2026-09-10 -->

<!-- build-audit: rev-217 verified at 2026-09-10 -->

<!-- build-audit: rev-218 verified at 2026-09-11 -->

<!-- build-audit: rev-219 verified at 2026-09-15 -->

<!-- build-audit: rev-220 verified at 2026-09-17 -->

<!-- build-audit: rev-221 verified at 2026-09-22 -->

<!-- build-audit: rev-223 verified at 2026-09-26 -->

<!-- build-audit: rev-224 verified at 2026-09-27 -->

<!-- build-audit: rev-225 verified at 2026-09-28 -->

<!-- build-audit: rev-226 verified at 2026-09-29 -->

<!-- build-audit: rev-227 verified at 2026-09-29 -->

<!-- build-audit: rev-228 verified at 2026-09-30 -->

<!-- build-audit: rev-229 verified at 2026-10-01 -->

<!-- build-audit: rev-231 verified at 2026-10-05 -->

<!-- build-audit: rev-232 verified at 2026-10-05 -->

<!-- build-audit: rev-233 verified at 2026-10-06 -->

<!-- build-audit: rev-234 verified at 2026-10-09 -->

<!-- build-audit: rev-236 verified at 2026-10-10 -->

<!-- build-audit: rev-237 verified at 2026-10-12 -->

<!-- build-audit: rev-238 verified at 2026-10-12 -->

<!-- build-audit: rev-239 verified at 2026-10-13 -->

<!-- build-audit: rev-241 verified at 2026-10-15 -->

<!-- build-audit: rev-242 verified at 2026-10-16 -->
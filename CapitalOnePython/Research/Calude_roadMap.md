Congrats on the Capital One assessment, Sean! Let me build you a comprehensive Zero-to-Hero prep plan for a **Lead Data Engineer** CodeSignal assessment. Based on Capital One's stack and typical senior-level assessments, here's your full breakdown:

---

# 🎯 Capital One Lead Data Engineer — CodeSignal Prep Plan

---

## 📦 TOPIC 1: SQL & Data Querying

### SubTopic 1.1: Core SQL Foundations
- **1.1.1** SELECT, WHERE, ORDER BY, LIMIT
- **1.1.2** GROUP BY, HAVING
- **1.1.3** DISTINCT, aliases (AS)
- **1.1.4** NULL handling (IS NULL, COALESCE, NULLIF)

### SubTopic 1.2: Joins & Set Operations
- **1.2.1** INNER, LEFT, RIGHT, FULL OUTER JOIN
- **1.2.2** CROSS JOIN & self-joins
- **1.2.3** UNION, UNION ALL, INTERSECT, EXCEPT
- **1.2.4** Multi-table join chaining

### SubTopic 1.3: Window Functions ⭐ (Heavy focus for senior roles)
- **1.3.1** ROW_NUMBER(), RANK(), DENSE_RANK()
- **1.3.2** LAG(), LEAD()
- **1.3.3** SUM(), AVG(), COUNT() OVER(PARTITION BY … ORDER BY …)
- **1.3.4** FIRST_VALUE(), LAST_VALUE(), NTILE()
- **1.3.5** Frame clauses: ROWS BETWEEN, RANGE BETWEEN

### SubTopic 1.4: Subqueries & CTEs
- **1.4.1** Scalar subqueries
- **1.4.2** Correlated subqueries
- **1.4.3** EXISTS / NOT EXISTS
- **1.4.4** WITH (CTEs) — single and recursive
- **1.4.5** CTEs vs subqueries vs temp tables — when to use which

### SubTopic 1.5: Advanced SQL Patterns
- **1.5.1** Running totals & moving averages
- **1.5.2** Pivoting / unpivoting data
- **1.5.3** Gap-and-island problems
- **1.5.4** Deduplication strategies
- **1.5.5** Date/time arithmetic (DATEDIFF, DATE_TRUNC, EXTRACT)

### SubTopic 1.6: Query Optimization
- **1.6.1** EXPLAIN / EXPLAIN ANALYZE
- **1.6.2** Index types and usage
- **1.6.3** Avoiding full table scans
- **1.6.4** Partition pruning
- **1.6.5** Query cost estimation basics

---

## 📦 TOPIC 2: Python for Data Engineering

### SubTopic 2.1: Python Core (Speed Round)
- **2.1.1** List/dict/set comprehensions
- **2.1.2** Lambda, map, filter, reduce
- **2.1.3** Generators and iterators
- **2.1.4** Decorators
- **2.1.5** Exception handling patterns
- **2.1.6** Context managers (with statements)

### SubTopic 2.2: Data Manipulation with Pandas
- **2.2.1** DataFrame creation, indexing, slicing
- **2.2.2** groupby, agg, transform, apply
- **2.2.3** merge, join, concat
- **2.2.4** Handling missing data (fillna, dropna, interpolate)
- **2.2.5** Pivot tables and crosstabs
- **2.2.6** Time series resampling

### SubTopic 2.3: Algorithms & Data Structures (CodeSignal-specific)
- **2.3.1** Arrays & strings (sliding window, two-pointer)
- **2.3.2** Hash maps / frequency counting
- **2.3.3** Sorting algorithms & custom sort keys
- **2.3.4** Binary search
- **2.3.5** Stacks, queues, deques
- **2.3.6** Recursion & memoization
- **2.3.7** Graph traversal (BFS/DFS) — rare but possible

### SubTopic 2.4: File & Data I/O
- **2.4.1** CSV, JSON, Parquet reading/writing
- **2.4.2** Working with APIs (requests)
- **2.4.3** File parsing and transformation patterns
- **2.4.4** Encoding/decoding (UTF-8, base64)

### SubTopic 2.5: OOP & Design Patterns
- **2.5.1** Classes, inheritance, polymorphism
- **2.5.2** Abstract base classes
- **2.5.3** Factory, Singleton, Strategy patterns
- **2.5.4** Dataclasses and type hints

---

## 📦 TOPIC 3: Data Pipeline & ETL Design

### SubTopic 3.1: ETL Fundamentals
- **3.1.1** Extract strategies (batch vs streaming, full vs incremental)
- **3.1.2** Transformation patterns (normalization, enrichment, aggregation)
- **3.1.3** Load strategies (upsert, SCD Type 1/2, append)
- **3.1.4** Idempotency and re-runnability

### SubTopic 3.2: Pipeline Architecture Patterns
- **3.2.1** Lambda architecture (batch + speed layer)
- **3.2.2** Kappa architecture (stream-only)
- **3.2.3** Medallion architecture (Bronze / Silver / Gold)
- **3.2.4** Data contracts and schema enforcement
- **3.2.5** Dead letter queues & error handling

### SubTopic 3.3: Orchestration
- **3.3.1** DAG concepts and dependency management
- **3.3.2** Airflow operators, sensors, hooks
- **3.3.3** Backfill, retry, and SLA strategies
- **3.3.4** Parameterized pipelines
- **3.3.5** Alternatives: Prefect, Dagster concepts

### SubTopic 3.4: Data Quality & Testing
- **3.4.1** Completeness, accuracy, consistency, timeliness checks
- **3.4.2** Schema validation (Great Expectations, Pandera)
- **3.4.3** Unit testing ETL functions (pytest, mocking)
- **3.4.4** Data reconciliation patterns
- **3.4.5** Monitoring & alerting on pipeline failures

---

## 📦 TOPIC 4: Cloud & Big Data (AWS focus — Capital One is heavily AWS)

### SubTopic 4.1: AWS Core Services for Data Engineering
- **4.1.1** S3 (partitioning, lifecycle, versioning, event triggers)
- **4.1.2** Glue (ETL jobs, Data Catalog, crawlers)
- **4.1.3** Athena (querying S3 with SQL, partitioning)
- **4.1.4** Redshift (distribution styles, sort keys, WLM)
- **4.1.5** Lambda (event-driven data processing)
- **4.1.6** Kinesis (Streams vs Firehose vs Analytics)
- **4.1.7** EMR (Spark on AWS)

### SubTopic 4.2: Big Data Processing with Spark
- **4.2.1** RDD vs DataFrame vs Dataset
- **4.2.2** Transformations (lazy) vs Actions (eager)
- **4.2.3** Partitioning and shuffling
- **4.2.4** Spark SQL and DataFrame API
- **4.2.5** Broadcast joins vs sort-merge joins
- **4.2.6** Caching and persistence strategies
- **4.2.7** PySpark UDFs (and why to avoid them)

### SubTopic 4.3: Storage Formats & Optimization
- **4.3.1** Parquet vs ORC vs Avro vs JSON — when to use each
- **4.3.2** Columnar storage benefits
- **4.3.3** Compression codecs (Snappy, GZIP, ZSTD)
- **4.3.4** Delta Lake / Iceberg / Hudi (table formats)
- **4.3.5** Partitioning strategies (date, region, category)

### SubTopic 4.4: Data Warehousing Concepts
- **4.4.1** Star schema vs snowflake schema
- **4.4.2** Fact vs dimension tables
- **4.4.3** SCD Type 1, 2, 3
- **4.4.4** Data vault basics
- **4.4.5** OLAP vs OLTP trade-offs

---

## 📦 TOPIC 5: System Design for Data Engineering ⭐ (Lead-level focus)

### SubTopic 5.1: Scalable Pipeline Design
- **5.1.1** Designing for high-volume ingestion (100M+ rows/day)
- **5.1.2** Horizontal vs vertical scaling decisions
- **5.1.3** Handling late-arriving data
- **5.1.4** Event sourcing and CQRS basics
- **5.1.5** Backpressure management

### SubTopic 5.2: Real-Time & Streaming Systems
- **5.2.1** Kafka architecture (topics, partitions, consumer groups)
- **5.2.2** Exactly-once vs at-least-once vs at-most-once semantics
- **5.2.3** Watermarks and windowing (tumbling, sliding, session)
- **5.2.4** Flink vs Spark Streaming trade-offs

### SubTopic 5.3: Data Governance & Security
- **5.3.1** PII detection and masking strategies (critical for Capital One / fintech)
- **5.3.2** Role-based access control (RBAC) on data
- **5.3.3** Column-level and row-level security
- **5.3.4** Data lineage and cataloging
- **5.3.5** GDPR / CCPA compliance patterns
- **5.3.6** Encryption at rest vs in transit

### SubTopic 5.4: Reliability & Observability
- **5.4.1** SLAs, SLOs, SLIs for data pipelines
- **5.4.2** Idempotency patterns
- **5.4.3** Circuit breakers and retry logic
- **5.4.4** Distributed tracing for pipelines
- **5.4.5** Logging best practices (structured logging)

---

## 📦 TOPIC 6: CodeSignal Platform-Specific Strategy

### SubTopic 6.1: Time Management (70 min)
- **6.1.1** Triage all questions first (30 seconds each)
- **6.1.2** Easy wins first — don't get stuck on hard problems early
- **6.1.3** Aim for a working brute-force before optimizing
- **6.1.4** Leave 5 min to review and clean up

### SubTopic 6.2: Code Quality Under Pressure
- **6.2.1** Use meaningful variable names even under time pressure
- **6.2.2** Add brief inline comments for logic
- **6.2.3** Handle edge cases (empty input, None, 0, single element)
- **6.2.4** Test with simple examples before submitting

### SubTopic 6.3: Environment Familiarity
- **6.3.1** Practice in CodeSignal IDE before the actual test
- **6.3.2** Know keyboard shortcuts for your language
- **6.3.3** Understand how test cases are structured and scored
- **6.3.4** Partial credit — a working O(n²) beats a broken O(n log n)

---

## 🗓️ RECOMMENDED STUDY SCHEDULE (10 Days to Feb 23)

| Day | Focus |
|-----|-------|
| **Day 1** | SQL: Joins, GROUP BY, aggregations — LeetCode easy/medium SQL |
| **Day 2** | SQL: Window functions deep dive — 10 practice problems |
| **Day 3** | SQL: CTEs, subqueries, query optimization |
| **Day 4** | Python: Arrays, hashmaps, sliding window — 8 CodeSignal problems |
| **Day 5** | Python: Pandas — data manipulation exercises |
| **Day 6** | ETL Design + Pipeline architecture concepts |
| **Day 7** | AWS services review + Spark fundamentals |
| **Day 8** | System design: 2 mock design sessions (streaming pipeline + data warehouse) |
| **Day 9** | Full mock CodeSignal timed session (70 min) |
| **Day 10** | Light review + rest + logistics prep (ID, camera, quiet room) |

---

## 🔗 Best Practice Resources

- **SQL Practice:** LeetCode SQL, Mode Analytics SQL Tutorial, SQLZoo
- **Python/Algo:** CodeSignal Arcade, LeetCode Medium (arrays, hashmaps, strings)
- **Spark/AWS:** AWS Skill Builder (free), Databricks Academy
- **System Design:** "Designing Data-Intensive Applications" (Kleppmann) — chapters on batch/stream processing

---

Want me to go deeper on any specific topic — for example, generate **practice SQL problems**, a **Spark cheat sheet**, or a **mock system design scenario** for Capital One's fintech context?
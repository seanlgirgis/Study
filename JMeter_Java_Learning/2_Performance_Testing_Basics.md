# 2. Performance Testing Basics Refresher

## The "What"
Performance testing is not just "bombarding the server." It is about understanding how the system behaves under specific conditions.

## Key Metrics (The "Language" of Performance)

### 1. Throughput (TPS / RPM)
-   **TPS**: Transactions Per Second.
-   **RPM**: Requests Per Minute.
-   *Analogy*: How many cars pass through a toll booth per minute.
-   *Goal*: Higher is better (usually).

### 2. Latency / Response Time
-   **Time To First Byte (TTFB)**: Time from sending the request to receiving the first part of the response.
-   **Total Response Time**: Time until the file download is complete.
-   *Analogy*: How long you wait in line at the toll booth.
-   *Goal*: Lower is better.

### 3. Concurrency (Virtual Users)
-   How many users are performing actions *at the exact same moment*.
-   *Note*: 1000 "Active Users" on a site might only mean 50 "Concurrent Users" hitting the submit button simultaneously.

### 4. Error Rate
-   Percentage of requests that fail (500 Server Error, 503 Unavailable, 408 Timeout).
-   *Goal*: Should be 0% under normal load.

## Types of Tests
1.  **Load Test**: "Can we handle expected traffic?" (e.g., 100 users).
2.  **Stress Test**: "When do we break?" (e.g., 1000 users... 2000 users... crash).
3.  **Soak / Endurance Test**: "Can we run for 24 hours without memory leaks?"
4.  **Spike Test**: "Can we survive a sudden jump in traffic?" (e.g., Black Friday sale start).

## The "Knee" of the Curve
When you graph **Throughput** vs. **Users**, it goes up linearly... until it doesn't.
-   **Pre-saturation**: Adding users increases throughput. latency is stable.
-   **Saturation Point (The Knee)**: Adding users does *not* increase throughput. Latency starts to spike.
-   **Crash**: Errors start occurring.

**Our Goal with JMeter**: Find that "Knee".

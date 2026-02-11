# 3. JMeter Introduction

## What is Apache JMeter?
A pure Java application designed to load test functional behavior and measure performance. It simulates a group of users sending requests to a target server.

## Core Elements of a Test Plan

### 1. Test Plan
The container for everything.

### 2. Thread Group (The "Users")
This represents the users. You define:
-   **Number of Threads (Users)**: e.g., 10.
-   **Ramp-up Period**: How long to take to start all threads. (e.g., 10 users in 10 seconds = 1 new user every second).
-   **Loop Count**: How many times each user performs the tasks.

### 3. Samplers (The "Actions")
What the user actually *does*.
-   **HTTP Request**: Most common. GET, POST, PUT, DELETE.
-   **JDBC Request**: Direct database query testing.
-   **Debug Sampler**: Outputs variable values (good for learning).

### 4. Logic Controllers (The "Flow")
-   **Simple Controller**: Groups requests.
-   **Loop Controller**: Repeats sub-items.
-   **If Controller**: Conditional logic.
-   **Transaction Controller**: Groups multiple requests into one "Transaction" time (e.g., Login + Browse + Checkout = "Buy Process").

### 5. Listeners (The "Results")
How you view the data.
-   **View Results Tree**: Shows Request/Response data (Heavy memory usage! Use for debug only).
-   **Summary Report**: Tabular data of throughput, min/max/avg response time.
-   **Graph Results**: Simple plotting.

## Best Practices
1.  **GUI Mode**: Use only for creating and debugging the test script.
2.  **CLI (Non-GUI) Mode**: Use for actual load testing.
    -   `jmeter -n -t test.jmx -l results.csv`
3.  **Listeners**: Disable "View Results Tree" during actual heavy load tests to save memory.

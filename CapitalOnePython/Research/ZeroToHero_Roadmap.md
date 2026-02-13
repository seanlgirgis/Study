# Capital One Lead Data Engineer — Master Roadmap (Zero to True Hero)

**Goal:** Ace the CodeSignal Assessment (Feb 23 Deadline) & Prepare for Power Day.
**Immediate Priority:** 10-Day Sprint for the 70-minute Coding Assessment (GCA).

---

## 📅 Part 1: The Critical Sprint (Feb 13 - Feb 23)
*Focus: Passing the 70-minute, 4-Question Proctored CodeSignal Assessment.*
*Format: Python 3 Algorithmic Coding (No GenAI).*

### 🧱 Phase 1.1: The Essentials (Days 1-3)
**Objective:** Guarantee 100% on Q1 and Q2 (< 15 mins total).
*   **Arrays & Strings:**
    *   `LeetCode 217`: Contains Duplicate.
    *   `LeetCode 242`: Valid Anagram.
    *   `LeetCode 1`: Two Sum.
*   **HashMap Mastery:**
    *   `LeetCode 49`: Group Anagrams.
    *   `LeetCode 974`: Subarray Sums Divisible by K.
*   **Simulation / Implementation (Capital One Favorite):**
    *   `LeetCode 2043`: **Simple Bank System**. (Must Do)
    *   `LeetCode 1603`: Design Parking System.

### 🕸️ Phase 1.2: The "Matrix Killer" (Days 4-6)
**Objective:** Survive Q3 (The most common failure point).
*   **Matrix Traversal:**
    *   `LeetCode 54`: **Spiral Matrix**.
    *   `LeetCode 48`: Rotate Image.
    *   `LeetCode 73`: Set Matrix Zeroes.
    *   `CodeSignal`: "Minimum Operations to Write the Letter Y on a Grid".
*   **BFS/DFS on Grid:**
    *   `LeetCode 200`: Number of Islands.
    *   `LeetCode 994`: Rotting Oranges.

### 🚀 Phase 1.3: Optimization & High Scores (Days 7-9)
**Objective:** Crack Q4 (CodeSignal Score 750+).
*   **Intervals & Greedy:**
    *   `LeetCode 56`: **Merge Intervals**.
    *   `LeetCode 937`: Reorder Data in Log Files.
*   **Monotonic Stack (Common Optimization):**
    *   `LeetCode 739`: Daily Temperatures.
    *   `LeetCode 84`: Largest Rectangle in Histogram.
*   **Advanced Simulation:**
    *   `LeetCode 3161`: Block Placement Queries.

### 🎓 Phase 1.4: Mock Exams (Day 10)
*   Take 2 Full 70-minute Simulated Exams on CodeSignal Arcade.

---

## 🏛️ Part 2: The "Data" Competency (Power Day Prep)
*Focus: SQL, Spark, and System Design for the On-Site/Final Round.*
*Note: Occasionally, Q4 in CodeSignal can be a complex SQL query.*

### 💾 Topic 2.1: Advanced SQL Patterns
*   **Window Functions:** `ROW_NUMBER()`, `RANK()`, `LEAD()`, `LAG()`.
    *   *Problem:* "Find the top 3 transaction amounts per user per month."
*   **Gaps & Islands:** Finding streaks of days with transactions.
*   **Joins:** Self-Joins, Cross Joins (for generating missing dates).

### ⚡ Topic 2.2: Big Data & PySpark
*   **Optimization:** Broadcast Joins vs Sort-Merge Joins.
*   **Skew Handling:** Salting keys.
*   **File Formats:** Parquet vs CSV (Push-down predicates).

### 🏗️ Topic 2.3: Data System Design
*   **Scenario:** "Design a real-time fraud detection pipeline for 100M transactions/day."
*   **Components:** Kafka (Ingest) -> Flink/Spark Streaming (Process) -> Cassandra (State) -> Snowflake (Warehousing).

---

## 📚 Resources & Cheat Sheets

### 🐍 Python Tricks for Speed
*   **Sorting:** `data.sort(key=lambda x: (x[0], -x[1]))` (Sort primary asc, secondary desc).
*   **Frequency:** `from collections import Counter`.
*   **Default Dict:** `from collections import defaultdict`.
*   **Heaps:** `import heapq` (Min-heap by default. Multiply by -1 for Max-heap).

### 📓 SQL Quick Reference
```sql
-- Window Function Syntax
SELECT *, 
       ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date DESC) as rn 
FROM transactions;
```

---

## ✅ Success Criteria
*   [ ] **Reliability:** Can solve `Simple Bank System` in < 15 mins.
*   [ ] **Matrix:** Can write `Spiral Matrix` without off-by-one errors.
*   [ ] **Speed:** Can recognize a "Sliding Window" problem instantly.
*   [ ] **Testing:** Always tests `Empty Input`, `Single Element`, and `Max Constraints` before submitting.

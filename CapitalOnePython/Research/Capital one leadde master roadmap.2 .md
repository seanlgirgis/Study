# 🏦 Capital One Lead Data Engineer — Zero to Super Hero
## The Definitive CodeSignal + Power Day Master Roadmap
**Deadline: February 23, 2026 | Assessment: 70 Minutes, 4 Questions, Proctored GCA**

---

> **Ground Truth from 2024–2026 Candidate Reports (Glassdoor, Blind, Prepfully, CodeSignal Docs):**
> - Format: **4 questions, 70 minutes, Python preferred**, proctored (camera + screen + mic + ID)
> - Q1 = Easy | Q2 = Easy-Medium | Q3 = Matrix/Grid KILLER (BFS/DFS — most failure point) | Q4 = Medium-Hard
> - **Winning strategy confirmed by passers:** Solve Q1 → Q2 → Q4 → return to Q3 if time remains
> - Score 500+ to advance (≈ 3 full solves + partial on 4th). Target 750+ for Lead-level impression
> - **It is 100% algorithmic DSA** — NOT SQL, Pandas, Spark, or ETL. Those come at Power Day
> - One DE candidate wrote: *"4 ridiculous questions that had NOTHING to do with what a data engineer does"* — confirmed by multiple reports
> - A staff-level engineer called it *"potentially the most difficult coding interview"* across multiple FAANG processes
> - CodeSignal reuses questions — practice the [CodeSignal Arcade](https://app.codesignal.com/arcade) **now**
> - **Partial credit is generous** (post-Spring 2023 scoring) — always submit something, even brute force
> - New scoring scale: **200–600** (not the old 300–850)

---

## 📋 TABLE OF CONTENTS

```
PART 1: THE 10-DAY SPRINT (CodeSignal GCA — Feb 13–23)
  Phase A: Foundation Tier    — Arrays, Strings, Hashing
  Phase B: Bread-and-Butter   — Two Pointers, Sliding Window, Sorting
  Phase C: Matrix Killer       — 2D Grid, BFS/DFS, Transformations
  Phase D: Score Differentiators — DP, Monotonic Stack, Binary Search
  Phase E: Python Mastery      — Modern Python 3.10+ Standards
  Phase F: CodeSignal Strategy — Test-Day Execution

PART 2: POWER DAY PREP (Post-CodeSignal)
  Topic 2.1: Advanced SQL
  Topic 2.2: Big Data & PySpark
  Topic 2.3: AWS Cloud Architecture
  Topic 2.4: Data System Design
  Topic 2.5: Capital One Fintech Context
  Topic 2.6: Behavioral / STAR

APPENDIX: Python Quick-Reference Cheat Sheet
```

---

# PART 1: THE 10-DAY SPRINT
## Focus: Passing the CodeSignal GCA (70-min, 4-Question, Python)

---

## 🧱 PHASE A: FOUNDATION TIER
### *Guarantee Q1 solved in < 10 min. Q2 in < 15 min.*

---

### A.1 Arrays & Lists

#### A.1.1 Traversal Patterns
- Linear scan with index tracking
- Reverse traversal (`range(n-1, -1, -1)`)
- Neighbor comparison (arr[i] vs arr[i-1])
- Simultaneous multi-pointer traversal

#### A.1.2 Prefix Sums (a.k.a. Partial Sums / Cumulative Sum)
- Build prefix array: `prefix[i] = prefix[i-1] + arr[i]`
- Range sum query: `sum(i, j) = prefix[j] - prefix[i-1]`
- **LeetCode 303** — Range Sum Query (Immutable)
- **LeetCode 560** — Subarray Sum Equals K
- **LeetCode 974** — Subarray Sums Divisible by K ⭐ (Capital One reported)

#### A.1.3 Suffix Sums & Products
- `suffix[i] = suffix[i+1] * arr[i]`
- **LeetCode 238** — Product of Array Except Self (no division)

#### A.1.4 Running Totals & Cumulative Logic
- Max so far, min so far patterns
- Kadane's Algorithm — Maximum Subarray Sum
  - `max_sum = max(arr[i], max_sum + arr[i])`
  - **LeetCode 53** — Maximum Subarray ⭐ (Capital One reported)

#### A.1.5 Counting & Frequency
- `collections.Counter` for O(n) frequency
- Bucket counting when value range is bounded
- **LeetCode 217** — Contains Duplicate
- **LeetCode 1** — Two Sum

#### A.1.6 Alternating / Parity Patterns
- Even/odd index conditions
- Sign alternation, zigzag arrays
- **LeetCode 376** — Wiggle Subsequence

---

### A.2 Strings

#### A.2.1 Character Frequency & Anagrams
- `Counter(s) == Counter(t)` for anagram check
- Sliding window counter comparison
- **LeetCode 242** — Valid Anagram ⭐
- **LeetCode 49** — Group Anagrams ⭐
- **LeetCode 438** — Find All Anagrams in a String

#### A.2.2 Substring Search & Pattern Matching
- Brute force O(n·m) — always implement first
- KMP (Knuth-Morris-Pratt) Algorithm — O(n+m)
  - Failure function / partial match table
- Rabin-Karp (Rolling Hash) — O(n) average
- **LeetCode 28** — Find the Index of the First Occurrence
- **LeetCode 459** — Repeated Substring Pattern

#### A.2.3 String Splitting, Joining, Parsing
- `str.split()`, `" ".join(list)`, `str.strip()`
- Tokenization by delimiter
- CSV-style parsing logic
- **LeetCode 937** — Reorder Data in Log Files ⭐ (Capital One reported)
- **LeetCode 1047** — Remove All Adjacent Duplicates

#### A.2.4 String Manipulation
- Palindrome detection (`s == s[::-1]`, two-pointer)
- Reverse words: `" ".join(s.split()[::-1])`
- Case manipulation, char replacement
- **LeetCode 5** — Longest Palindromic Substring
- **LeetCode 125** — Valid Palindrome

#### A.2.5 String Encoding / Simulation
- Run-length encoding
- Caesar cipher rotation
- Vowel/consonant classification patterns
- CodeSignal's own pattern-matching sample (vowel=0, consonant=1)

---

### A.3 Hashing & Hash Maps

#### A.3.1 HashMap / Dictionary Fundamentals
- `dict.get(key, default)` — safe lookup
- `collections.defaultdict(int)` — auto-zero
- `collections.defaultdict(list)` — auto-list
- `collections.Counter` — sorted most_common(k)

#### A.3.2 Two-Sum / Complement Patterns
- Store seen values: `seen[target - num]`
- **LeetCode 1** — Two Sum ⭐
- **LeetCode 167** — Two Sum II (sorted)
- **LeetCode 15** — 3Sum (sort + two-pointer)

#### A.3.3 Grouping & Bucketing
- Group by computed key (e.g., sorted chars for anagrams)
- `defaultdict(list)` bucket grouping
- **LeetCode 49** — Group Anagrams ⭐
- **LeetCode 128** — Longest Consecutive Sequence (O(n) with set)

#### A.3.4 Frequency Analysis
- Top-K elements: `Counter.most_common(k)` or `heapq.nlargest`
- **LeetCode 347** — Top K Frequent Elements
- **LeetCode 451** — Sort Characters By Frequency

#### A.3.5 Existence / Membership Checks
- Set for O(1) lookup: `if x in seen_set`
- Complement search in O(1)
- **LeetCode 217** — Contains Duplicate

---

### A.4 Object-Oriented Simulation (Capital One LOVES These)

#### A.4.1 Class-Based State Machines
- `__init__`, `__repr__`, `__str__`
- Instance variables for internal state
- Method dispatch based on input type

#### A.4.2 Banking System Simulation ⭐ (CONFIRMED Capital One Pattern)
- Account balance tracking
- Deposit / Withdrawal / Transfer with validation
- Overdraft and invalid state handling
- **LeetCode 2043** — Simple Bank System ⭐ MUST DO
- **LeetCode 1603** — Design Parking System
- **LeetCode 622** — Design Circular Queue
- **LeetCode 155** — Min Stack

#### A.4.3 Design Patterns in Simulation
- Singleton (one instance manages shared state)
- Factory (create objects by type)
- Strategy (swap algorithms at runtime)

---

## 🥖 PHASE B: BREAD-AND-BUTTER TIER
### *Must solve Q2 cleanly. Often appears in Q4 too.*

---

### B.1 Two Pointers

#### B.1.1 Opposite-End Pointers (Sorted Arrays)
- Left/right converging: `l, r = 0, n-1`
- Classic squeeze pattern
- **LeetCode 167** — Two Sum II
- **LeetCode 11** — Container With Most Water ⭐ (reported Capital One)
- **LeetCode 42** — Trapping Rain Water (see Monotonic Stack too)

#### B.1.2 Same-Direction Pointers
- Fast/slow pointer (Floyd's Cycle Detection)
  - Linked list cycle: `slow, fast = head, head`
- Remove duplicates in-place
- **LeetCode 26** — Remove Duplicates from Sorted Array
- **LeetCode 141** — Linked List Cycle

#### B.1.3 Three Pointers / Multi-Pointer
- Dutch National Flag (0/1/2 sorting)
  - `lo, mid, hi` with single pass
- **LeetCode 75** — Sort Colors
- **LeetCode 15** — 3Sum

#### B.1.4 Partition Patterns
- Lomuto / Hoare partition (QuickSort basis)
- In-place odd/even rearrangement
- **LeetCode 905** — Sort Array By Parity

---

### B.2 Sliding Window

#### B.2.1 Fixed-Size Window
- Maintain window sum: `window_sum = window_sum + arr[i] - arr[i-k]`
- Maximum/minimum of each window
- **LeetCode 643** — Maximum Average Subarray I
- **LeetCode 239** — Sliding Window Maximum (Monotonic Deque)

#### B.2.2 Variable-Size Window (Expand/Contract)
- Expand right: `r += 1`
- Contract left when condition violated: `l += 1`
- **LeetCode 3** — Longest Substring Without Repeating Characters ⭐
- **LeetCode 76** — Minimum Window Substring (hard)
- **LeetCode 424** — Longest Repeating Character Replacement
- **LeetCode 567** — Permutation in String

#### B.2.3 Substring / Subarray with Constraints
- At-most-K distinct chars pattern
- Binary condition windows (count of 1s / 0s)
- **LeetCode 992** — Subarrays with K Different Integers
- **LeetCode 1004** — Max Consecutive Ones III

#### B.2.4 Moving Average (Streaming Pattern)
- Deque-based window for streaming data
- **LeetCode 346** — Moving Average from Data Stream (Premium)

---

### B.3 Sorting & Custom Comparators

#### B.3.1 Built-in Sorts
- `arr.sort()` — in-place, Timsort, O(n log n)
- `sorted(arr)` — returns new list
- Stable sort property (preserves relative order of equals)

#### B.3.2 Custom Sort Keys (Lambda)
- Single key: `arr.sort(key=lambda x: x[1])`
- Multi-key: `arr.sort(key=lambda x: (x[0], -x[1]))` — asc primary, desc secondary ⭐
- Sort strings by length then alpha: `key=lambda s: (len(s), s)`

#### B.3.3 Interval Problems
- Sort by start: `intervals.sort(key=lambda x: x[0])`
- Merge overlapping: check `current[1] >= next[0]`
- **LeetCode 56** — Merge Intervals ⭐ (Capital One reported)
- **LeetCode 57** — Insert Interval
- **LeetCode 435** — Non-overlapping Intervals (Greedy)
- **LeetCode 252/253** — Meeting Rooms I & II

#### B.3.4 Counting Sort & Bucket Sort
- When value range is bounded (O(n) sort)
- Frequency array as sort
- **LeetCode 75** — Sort Colors (counting sort version)

#### B.3.5 Heap-Based Sorting (Top-K)
- `import heapq` — min-heap by default
- Max-heap trick: insert `-value`
- `heapq.nlargest(k, iterable)` / `heapq.nsmallest(k, iterable)`
- **LeetCode 347** — Top K Frequent Elements ⭐
- **LeetCode 215** — Kth Largest Element in Array

---

### B.4 Greedy Algorithms

#### B.4.1 Activity Selection / Interval Scheduling
- Sort by end time, always pick earliest finish
- **LeetCode 435** — Non-Overlapping Intervals

#### B.4.2 Jump Game Variants
- Track `max_reach` from left
- **LeetCode 55** — Jump Game
- **LeetCode 45** — Jump Game II (minimum jumps)

#### B.4.3 Task Scheduling
- Most frequent task determines idle time
- `Counter` + max frequency logic
- **LeetCode 621** — Task Scheduler

#### B.4.4 Greedy on Strings
- Remove k digits for smallest number
- Monotonic greedy approach
- **LeetCode 402** — Remove K Digits
- **LeetCode 316** — Remove Duplicate Letters

---

## 🕷️ PHASE C: MATRIX KILLER TIER
### *Q3 is almost always here. Decide: full attempt or triage + skip. Never waste >25 min.*

---

### C.1 Matrix Traversal Fundamentals

#### C.1.1 Row/Column/Diagonal Traversal
- Row-major: `for i in range(m): for j in range(n):`
- Column-major: transpose indices
- Main diagonal: `(i, j)` where `i == j`
- Anti-diagonal: `(i, j)` where `i + j == n-1`

#### C.1.2 Spiral Order Traversal ⭐ (Top Q3 Pattern)
- Four boundary pointers: `top, bottom, left, right`
- Shrink boundaries after each direction pass
- **LeetCode 54** — Spiral Matrix ⭐ MUST DO
- **LeetCode 59** — Spiral Matrix II (generate)

#### C.1.3 Zigzag / Diagonal Traversal
- Direction flip on boundary hit
- **LeetCode 498** — Diagonal Traverse

#### C.1.4 Boundary Walking
- Perimeter traversal pattern
- Layer-by-layer (onion peeling)

---

### C.2 Matrix Transformation

#### C.2.1 In-Place Rotation ⭐
- 90° clockwise = Transpose + Reverse each row
  - Step 1: `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`
  - Step 2: `row.reverse()` for each row
- 90° counter-clockwise = Reverse each row + Transpose
- **LeetCode 48** — Rotate Image ⭐ MUST DO

#### C.2.2 Transpose
- `zip(*matrix)` — Python one-liner transpose
- Manual swap: `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`

#### C.2.3 Set Zeroes (In-Place with O(1) space)
- Use first row/column as markers
- **LeetCode 73** — Set Matrix Zeroes ⭐

#### C.2.4 Letter/Pattern Writing on Grid
- **CodeSignal Specific** — "Minimum Operations to Write the Letter Y on a Grid" pattern
- Identify which cells belong to the shape, count mismatches

---

### C.3 BFS on Grid (Breadth-First Search)

#### C.3.1 BFS Template
```python
from collections import deque
def bfs(grid, start_r, start_c):
    m, n = len(grid), len(grid[0])
    queue = deque([(start_r, start_c)])
    visited = set([(start_r, start_c)])
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
```

#### C.3.2 Flood Fill / Connected Components
- Multi-source BFS (start all sources simultaneously)
- **LeetCode 200** — Number of Islands ⭐ MUST DO
- **LeetCode 733** — Flood Fill
- **LeetCode 695** — Max Area of Island

#### C.3.3 Shortest Path on Grid (Unweighted)
- BFS guarantees shortest path in unweighted graphs
- Level-by-level tracking (distance array)
- **LeetCode 994** — Rotting Oranges ⭐ (multi-source BFS)
- **LeetCode 1091** — Shortest Path in Binary Matrix

#### C.3.4 0-1 BFS (Deque-based)
- Edges weight 0 → prepend to deque
- Edges weight 1 → append to deque
- Used when moves have variable costs

---

### C.4 DFS on Grid (Depth-First Search)

#### C.4.1 DFS Template (Recursive)
```python
def dfs(grid, r, c, visited):
    m, n = len(grid), len(grid[0])
    if r < 0 or r >= m or c < 0 or c >= n: return
    if (r, c) in visited or grid[r][c] == 0: return
    visited.add((r, c))
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        dfs(grid, r+dr, c+dc, visited)
```

#### C.4.2 DFS Template (Iterative — avoids recursion limit)
```python
def dfs_iterative(grid, start_r, start_c):
    stack = [(start_r, start_c)]
    visited = set()
    while stack:
        r, c = stack.pop()
        if (r, c) in visited: continue
        visited.add((r, c))
        # process (r, c)
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            stack.append((r+dr, c+dc))
```

#### C.4.3 Island/Region Problems
- Mark visited in-place (modify grid) or use visited set
- **LeetCode 200** — Number of Islands
- **LeetCode 695** — Max Area of Island
- **LeetCode 130** — Surrounded Regions

#### C.4.4 Backtracking on Grid
- DFS + undo step after recursion
- **LeetCode 79** — Word Search ⭐
- **LeetCode 212** — Word Search II (Trie + DFS)

---

### C.5 Dynamic Programming on 2D Grid

#### C.5.1 Path Counting
- `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
- **LeetCode 62** — Unique Paths
- **LeetCode 63** — Unique Paths II (with obstacles)

#### C.5.2 Min/Max Path Cost
- `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`
- **LeetCode 64** — Minimum Path Sum
- **LeetCode 120** — Triangle (bottom-up)

#### C.5.3 Candy Crush / Game Simulation ⭐ (CONFIRMED Capital One Q3)
- Gravity simulation (bubbles falling)
- Match-3 elimination patterns
- Multi-pass simulation until stable
- This is the "ridiculous candy crush" question DE candidates reported!

---

## 🚀 PHASE D: SCORE DIFFERENTIATORS
### *Q4 territory. Partial credit here separates 500 from 750+*

---

### D.1 Dynamic Programming (DP)

#### D.1.1 The DP Framework
1. Define subproblem: what does `dp[i]` represent?
2. Recurrence relation: how does `dp[i]` depend on smaller subproblems?
3. Base cases: `dp[0]`, `dp[1]`
4. Order: bottom-up (iterative) preferred over top-down (memoization)
5. Space optimization: often can reduce to O(1) or O(n)

#### D.1.2 Classic 1D DP
- **House Robber** — `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
  - **LeetCode 198** — House Robber ⭐
  - **LeetCode 213** — House Robber II (circular)
- **Climbing Stairs** — `dp[i] = dp[i-1] + dp[i-2]` (Fibonacci)
  - **LeetCode 70** — Climbing Stairs
- **Coin Change** — `dp[i] = min(dp[i], dp[i-coin] + 1)`
  - **LeetCode 322** — Coin Change ⭐

#### D.1.3 Subarray / Subsequence DP
- **Maximum Product Subarray** — track max AND min (negatives flip)
  - **LeetCode 152** — Maximum Product Subarray
- **Longest Increasing Subsequence (LIS)** — O(n²) DP, O(n log n) with patience sorting
  - **LeetCode 300** — Longest Increasing Subsequence ⭐
- **Longest Common Subsequence (LCS)** — 2D DP
  - `dp[i][j] = dp[i-1][j-1]+1` if match, else `max(dp[i-1][j], dp[i][j-1])`
  - **LeetCode 1143** — Longest Common Subsequence

#### D.1.4 Knapsack Variants
- 0/1 Knapsack: `dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])`
- Unbounded Knapsack: item can be reused
- **LeetCode 416** — Partition Equal Subset Sum
- **LeetCode 518** — Coin Change II (combinations)

#### D.1.5 String DP
- Edit Distance (Levenshtein): insert/delete/replace operations
  - **LeetCode 72** — Edit Distance
- **LeetCode 139** — Word Break (dp[i] = any dp[j] + word[j:i])
- **LeetCode 516** — Longest Palindromic Subsequence

---

### D.2 Monotonic Stack

#### D.2.1 The Monotonic Stack Concept
- Maintains elements in strictly increasing or decreasing order
- Pops when invariant is violated — the pop event encodes useful info
- Two flavors: **Monotonic Increasing** (for next smaller) / **Monotonic Decreasing** (for next greater)

#### D.2.2 Next Greater Element (NGE)
```python
def next_greater(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # stores indices
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result
```
- **LeetCode 496** — Next Greater Element I
- **LeetCode 739** — Daily Temperatures ⭐ (Capital One reported)
- **LeetCode 503** — Next Greater Element II (circular)

#### D.2.3 Largest Rectangle in Histogram ⭐ (Capital One CONFIRMED)
- Use monotonic increasing stack of indices
- Pop when current bar shorter than stack top
- Area = `heights[popped] × (i - stack[-1] - 1)`
- **LeetCode 84** — Largest Rectangle in Histogram ⭐ MUST DO
- **LeetCode 85** — Maximal Rectangle (extends to matrix)

#### D.2.4 Trapping Rain Water
- Monotonic stack approach (or two-pointer)
- **LeetCode 42** — Trapping Rain Water ⭐

#### D.2.5 Monotonic Deque (Sliding Window Maximum)
- `collections.deque` maintaining decreasing order
- Front is always current window maximum
- **LeetCode 239** — Sliding Window Maximum

---

### D.3 Binary Search

#### D.3.1 Classic Binary Search Template
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2  # Avoids overflow (Python int is fine, but good habit)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### D.3.2 Leftmost / Rightmost Occurrence
- Find first: `hi = mid - 1` when found, continue
- Find last: `lo = mid + 1` when found, continue
- **LeetCode 34** — Find First and Last Position

#### D.3.3 Binary Search on Answer (Parametric Search) ⭐
- When answer is monotonic: "can we do it with X?"
- Pattern: `lo=min_possible, hi=max_possible` → binary search the answer
- **LeetCode 875** — Koko Eating Bananas ⭐
- **LeetCode 1011** — Capacity To Ship Packages Within D Days ⭐ (Capital One reported)
- **LeetCode 410** — Split Array Largest Sum
- **LeetCode 2064** — Minimized Maximum of Products Distributed

#### D.3.4 Binary Search on Rotated Arrays
- Identify which half is sorted, search there
- **LeetCode 33** — Search in Rotated Sorted Array
- **LeetCode 153** — Find Minimum in Rotated Sorted Array

---

### D.4 Graph Algorithms (Light — for Q3/Q4 edge cases)

#### D.4.1 Graph Representations
- Adjacency list: `defaultdict(list)`
- Adjacency matrix: `[[0]*n for _ in range(n)]`
- Edge list: `[(u, v, weight), ...]`

#### D.4.2 BFS (Breadth-First Search) — Shortest Path
- `collections.deque`, level-by-level
- Distance tracking: `dist = {start: 0}`
- **LeetCode 127** — Word Ladder (implicit graph BFS)
- **LeetCode 207** — Course Schedule (topological sort)

#### D.4.3 DFS — Connectivity & Cycle Detection
- Visited states: unvisited (0), in-progress (1), done (2)
- **LeetCode 207** — Course Schedule (DFS cycle detection)
- **LeetCode 210** — Course Schedule II (Kahn's Algorithm / topological sort)

#### D.4.4 Union-Find (Disjoint Set Union — DSU)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True
```
- **LeetCode 547** — Number of Provinces
- **LeetCode 684** — Redundant Connection

#### D.4.5 Dijkstra's Algorithm (Weighted Shortest Path)
- Priority queue (`heapq`) + distance array
- `heapq.heappush(pq, (dist, node))`
- **LeetCode 743** — Network Delay Time

---

## 🐍 PHASE E: Python Mastery
### *Modern Python 3.10+ Standards (Lead-Level Code Quality)*

---

### E.1 Type Hints & Annotations
- Function signatures: `def func(arr: list[int]) -> int:`
- Variables: `from typing import List, Dict, Optional`
- Strict typing: `TypedDict`, `dataclass`, `Annotated`
- **mypy** strict mode for type checking
- **LeetCode Tip:** Always add type hints to function params/return

### E.2 Pathlib for File Handling
- `from pathlib import Path`
- `path = Path('file.txt')`
- `path.read_text()`, `path.write_bytes(data)`
- Avoid `os.path` — use Path everywhere

### E.3 Advanced Collections
- `collections.deque` for O(1) pops from both ends
- `collections.namedtuple` / `dataclasses.dataclass` for structured data
- `heapq` for priority queues
- `bisect` for binary search on sorted lists

### E.4 Itertools & Functools
- `itertools.combinations(arr, k)`, `itertools.permutations`
- `itertools.product` for Cartesian product
- `functools.cache` / `lru_cache` for memoization
- `functools.partial` for currying functions

### E.5 List Comprehensions & Generators
- `[x**2 for x in arr if x > 0]`
- Generator: `(x**2 for x in arr)` — memory efficient
- Dict comp: `{k: v for k, v in pairs}`
- Set comp: `{x.lower() for x in strings}`

### E.6 Error Handling & Edge Cases
- `try: ... except ValueError: ...`
- Custom exceptions: `raise ValueError("Invalid input")`
- Always handle: empty lists, None, negative indices, overflow (Python ints are fine)

### E.7 Python 3.12 Features (Align with Style)
- Structural pattern matching: `match x: case [1,2]: ...`
- Better f-strings: `f"{value=}"` (self-documenting)
- Type aliases: `type Vector = list[float]`
- Improved error messages for better debugging

### E.8 Code Style Enforcement
- Black formatter (line-length 100)
- Ruff linter (strict)
- isort (black profile)
- Docstrings: Google/Numpy style, mandatory for functions/classes
- **Tip:** Use code_execution tool in Grok for quick testing/validation during practice

---

## 🎯 PHASE F: CodeSignal Strategy
### *Test-Day Execution*

---

### F.1 Pre-Test Preparation

#### F.1.1 Platform Familiarization
- Create CodeSignal account with application email
- Practice Arcade: 50+ problems, focus on "Interview Practice" section
- Take sample GCA: Simulate 70-min with proctoring enabled
- Review FAQs: Time limits, partial scoring, language selection (Python 3)

#### F.1.2 Mock Sessions
- Use LeetCode timed contests (4 problems, 70 min)
- Target: 3 full solves + partial on hard
- After each: Review time spent per question, optimize

#### F.1.3 Mental Prep
- Sleep 8 hrs night before
- No caffeine crash — light meal
- Quiet room, backup internet

### F.2 In-Test Execution

#### F.2.1 The First 2 Minutes (Triage)
1. Open ALL 4 problems, read each in 30 seconds
2. Mentally classify: Easy / Medium / Hard
3. Confirm Q1 is easy → start there
4. Note which Q3 pattern it is (spiral? flood fill? rotation?)
5. Set mental time limits: Q1=10, Q2=15, Q4=20, Q3=rest

#### F.2.2 Problem-Solving Protocol
```
1. Read → Understand → Restate in your words
2. Identify pattern (Two pointers? BFS? DP?)
3. Write brute force first — even O(n²) is better than nothing
4. Code the brute force — test with examples
5. Optimize only if time permits
6. ALWAYS SUBMIT — partial credit is real
```

#### F.2.3 When You're Stuck
- Stuck > 5 min → write down your approach, move on
- Stuck on Q3 > 18 min → write whatever partial you have, MOVE TO Q4
- Always leave at least some code per problem — even a stub + comment shows intent

#### F.2.4 Code Quality (Scores on quality, not just correctness)
- Meaningful variable names (even under pressure): `left_ptr` not `l`
- Type hints on function signatures
- Brief inline comment on non-obvious logic
- Handle edge cases BEFORE submitting
- Test 3 cases mentally: normal, empty, single element

---

### F.3 Scoring & Partial Credit

#### F.3.1 The Scoring Reality (Post-Spring 2023)
- Scale: **200–600** (old scale was 300–850)
- Target for Lead DE role: **500+ to advance** (≈ 3 full solves)
- A brute-force O(n²) on Q4 earns more partial credit than nothing
- Every test case you pass adds points — submit early and often

#### F.3.2 What Capital One Is Looking For at Lead Level
- **Not just correctness** — they want clean, production-grade thinking
- Edge case handling demonstrates senior instinct
- Readable code matters (they may review it in Power Day)

---

### F.4 Proctoring and Technical Setup (From 2025-2026 Reports)
- **Requirements:** Computer (no mobile), strong internet (500 kb/s+), up-to-date browser (Chrome/Firefox), webcam, microphone, screen-sharing, government-issued photo ID
- **Environment:** Quiet room, no disturbances, no one entering frame
- **Rules:** One sitting, no unauthorized resources (including GenAI/external help) — violations lead to disqualification or termination
- **Tips:** Test setup on CodeSignal practice mode; avoid firewalled networks (e.g., office WiFi); have backup device ready
- **Common Pitfalls:** Browser compatibility issues — test early; ensure email matches application for score reuse option

---

# PART 2: POWER DAY PREP
## What Comes After You Pass the CodeSignal

---

## 📊 TOPIC 2.1: Advanced SQL

### 2.1.1 Window Functions (Heavy Lead-Level Focus)
- `ROW_NUMBER()` — unique rank, no ties
- `RANK()` — ties get same rank, gaps after
- `DENSE_RANK()` — ties get same rank, no gaps
- `NTILE(n)` — divide into n buckets
- `LAG(col, offset, default)` / `LEAD(col, offset, default)` — access previous/next row
- `FIRST_VALUE(col)` / `LAST_VALUE(col)` — within window frame
- Frame clauses: `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`

**Power Day SQL Practice Problem:**
```sql
-- "Find the top 3 transaction amounts per user per month"
WITH ranked AS (
  SELECT 
    user_id,
    DATE_TRUNC('month', txn_date) AS month,
    amount,
    DENSE_RANK() OVER (
      PARTITION BY user_id, DATE_TRUNC('month', txn_date)
      ORDER BY amount DESC
    ) AS rk
  FROM transactions
)
SELECT * FROM ranked WHERE rk <= 3;
```

### 2.1.2 CTEs & Recursive CTEs
- Common Table Expressions for readability
- Recursive CTE for hierarchical data (org charts, paths)
```sql
WITH RECURSIVE org_tree AS (
  SELECT employee_id, manager_id, 1 AS level
  FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.employee_id, e.manager_id, o.level + 1
  FROM employees e JOIN org_tree o ON e.manager_id = o.employee_id
)
SELECT * FROM org_tree;
```

### 2.1.3 Gaps & Islands Problem
- Find consecutive sequences of dates/IDs
```sql
-- Mark each "island" by comparing to row_number
WITH numbered AS (
  SELECT date, ROW_NUMBER() OVER (ORDER BY date) AS rn
  FROM active_dates
)
SELECT MIN(date), MAX(date), COUNT(*) AS streak_length
FROM numbered
GROUP BY DATE(date) - rn * INTERVAL '1 day'  -- PostgreSQL
ORDER BY MIN(date);
```

### 2.1.4 Self-Joins & Cross Joins
- Employee/manager pairs: `e1 JOIN e2 ON e1.manager_id = e2.employee_id`
- Generate date ranges: CROSS JOIN calendar table
- Comparison of same-entity records across periods

### 2.1.5 Query Optimization (Capital One AWS/Redshift Context)
- `EXPLAIN ANALYZE` — actual vs estimated row counts
- Index types: B-Tree (range), Hash (equality), Partial (filtered)
- Partition pruning — ensure WHERE clause matches partition key
- Redshift-specific: distribution styles (`KEY`, `ALL`, `EVEN`), sort keys
- Avoid `SELECT *` — columnar storage is hurt by fetching all columns

---

## ⚡ TOPIC 2.2: Big Data & PySpark

### 2.2.1 Spark Architecture
- **Driver** — orchestrates job, holds SparkContext
- **Executors** — run tasks, hold data partitions
- **DAG (Directed Acyclic Graph)** — logical execution plan
- **Stage** — set of tasks with no shuffle boundary
- **Task** — smallest unit, runs on one partition

### 2.2.2 RDD vs DataFrame vs Dataset
- **RDD** — low-level, distributed collection, no schema, type-safe in Scala
- **DataFrame** — distributed table with schema, Spark SQL optimizable (Catalyst Optimizer)
- **Dataset** — typed DataFrame (Scala/Java only; in Python, DataFrame = Dataset[Row])
- **Always use DataFrame/Spark SQL in Python** — Catalyst optimizer works on it

### 2.2.3 Transformations (Lazy) vs Actions (Eager)
- **Lazy:** `map()`, `filter()`, `select()`, `groupBy()`, `join()`, `withColumn()`, `drop()`
- **Eager (trigger execution):** `collect()`, `count()`, `show()`, `write()`, `take(n)`
- Nothing runs until an action is called — the DAG is just a plan

### 2.2.4 Join Strategies
- **Broadcast Join (Map-Side Join)** — small table fits in memory, broadcast to all executors
  ```python
  from pyspark.sql.functions import broadcast
  df_large.join(broadcast(df_small), "key")
  ```
- **Sort-Merge Join** — both tables sorted and merged; default for large tables
- **Shuffle Hash Join** — hash-based; no sort needed; risky with skew
- Rule of thumb: `spark.sql.autoBroadcastJoinThreshold` (default 10MB)

### 2.2.5 Partitioning & Shuffling
- **Shuffle** = expensive data redistribution across network (caused by groupBy, join, distinct)
- **repartition(n)** — full shuffle to n partitions (use before joins/writes)
- **coalesce(n)** — reduce partitions without full shuffle (use before writing)
- **partitionBy("date")** — partition output files by column for partition pruning

### 2.2.6 Skew Handling (Salting Technique)
```python
from pyspark.sql.functions import col, concat, lit, rand, floor

# Add salt to skewed key
N_SALTS = 10
df_skewed = df.withColumn("salted_key", 
    concat(col("join_key"), lit("_"), (floor(rand() * N_SALTS)).cast("string")))

# Explode salt on small table
from pyspark.sql.functions import explode, array
df_small_exploded = df_small.withColumn("salt_range", array([lit(i) for i in range(N_SALTS)]))
df_small_exploded = df_small_exploded.withColumn("salt", explode("salt_range"))
df_small_exploded = df_small_exploded.withColumn("salted_key",
    concat(col("join_key"), lit("_"), col("salt").cast("string")))

result = df_skewed.join(df_small_exploded, "salted_key")
```

### 2.2.7 PySpark UDFs — When to Avoid
- Python UDFs: data serialized row-by-row between JVM and Python → slow
- **Prefer:** Built-in Spark SQL functions (`pyspark.sql.functions`)
- **If UDF needed:** Use Pandas UDF (Vectorized UDF) via `@pandas_udf`
```python
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import DoubleType
import pandas as pd

@pandas_udf(DoubleType())
def normalize(series: pd.Series) -> pd.Series:
    return (series - series.mean()) / series.std()

df = df.withColumn("normalized_score", normalize(df["score"]))
```

### 2.2.8 Caching & Persistence
- `df.cache()` = `df.persist(StorageLevel.MEMORY_AND_DISK)`
- Cache when DataFrame is used multiple times in the same job
- `df.unpersist()` — free memory when done
- Storage levels: `MEMORY_ONLY`, `MEMORY_AND_DISK`, `DISK_ONLY`

---

## ☁️ TOPIC 2.3: AWS Cloud Architecture (Capital One is 100% AWS)

### 2.3.1 Core Data Services
- **Amazon S3** — object storage; partition by `year=/month=/day=` for Athena/Glue performance
  - Lifecycle rules, versioning, event notifications (→ Lambda)
- **AWS Glue** — managed ETL; Glue Catalog = metadata store for Athena/Redshift Spectrum
  - Glue Crawlers auto-detect schema and partitions
  - Glue DataBrew — visual data prep (no-code)
- **Amazon Athena** — serverless SQL on S3 (Presto/Trino under the hood)
  - Partition projection — avoid costly crawl for well-known partition schemes
  - Workgroups — cost control and query isolation
- **Amazon Redshift** — columnar data warehouse
  - Distribution styles: `KEY` (join optimization), `ALL` (small dimension tables), `EVEN` (default)
  - Sort keys: compound vs interleaved
  - WLM (Workload Management) — queue prioritization
  - Redshift Spectrum — query S3 directly from Redshift

### 2.3.2 Streaming & Event-Driven
- **Amazon Kinesis Data Streams** — real-time streaming, shards (1MB/s in, 2MB/s out each)
- **Amazon Kinesis Data Firehose** — managed delivery to S3, Redshift, OpenSearch
- **Amazon Kinesis Data Analytics** — SQL or Apache Flink on streams
- **Amazon MSK (Managed Streaming for Apache Kafka)** — fully managed Kafka

### 2.3.3 Compute & Orchestration
- **AWS Lambda** — event-driven, serverless; max 15 min, 10GB RAM
- **Amazon EMR** — managed Hadoop/Spark; use EMR Serverless for auto-scaling
- **Amazon MWAA** — Managed Workflows for Apache Airflow
- **AWS Step Functions** — orchestrate Lambda + other services as state machines
- **AWS Glue Workflows** — orchestrate Glue jobs

### 2.3.4 Storage & Format Optimization
- **Parquet** — columnar, splittable, excellent for analytics
- **ORC** — columnar, good for Hive/Hudi
- **Avro** — row-based, great for schema evolution in Kafka
- **Delta Lake / Apache Iceberg** — ACID transactions on S3 (time travel, schema evolution)
  - Iceberg is AWS native (Athena + Glue support)
  - Delta Lake = Databricks ecosystem
  - Apache Hudi — incrementals, upserts (popular at Capital One for near-real-time)

---

## 🏗️ TOPIC 2.4: Data System Design

### 2.4.1 Real-Time Fraud Detection Pipeline (Capital One Flagship Scenario)
```
Architecture:
Transaction Events
  → Kinesis Data Streams (ingest at scale, sharding by card_id)
  → AWS Lambda / Kinesis Analytics with Flink
      ├── Feature extraction (velocity, geo-deviation, merchant risk)
      ├── ML model inference (SageMaker endpoint or embedded ONNX)
      └── Rule engine (real-time rule evaluation)
  → DynamoDB (< 1ms state lookups — account history, blacklists)
  → Decision Bus → Block/Allow → Card Network
  → Kinesis Firehose → S3 (Bronze layer, raw events)
  → Glue + Spark → S3 (Silver: cleaned, Gold: aggregated features)
  → Redshift / Athena (analyst queries, model retraining data)
```

### 2.4.2 Medallion Architecture (Bronze / Silver / Gold)
- **Bronze** — Raw ingest, immutable, append-only (parquet or JSON, partitioned by ingestion date)
- **Silver** — Cleansed, deduplicated, typed, enriched (Delta/Iceberg for ACID)
- **Gold** — Aggregated, domain-specific, query-optimized (fact/dimension, pre-joined)

### 2.4.3 Lambda Architecture
- **Batch Layer** — processes all historical data, slow but accurate (Spark on EMR)
- **Speed Layer** — processes recent data, fast but approximate (Kinesis + Flink)
- **Serving Layer** — merges batch + speed views (DynamoDB or Cassandra)

### 2.4.4 Kappa Architecture
- Eliminate batch layer — everything is streaming
- Kafka stores events permanently (configurable retention)
- Reprocess history by replaying Kafka from offset 0
- Simpler operationally; works when streaming can handle batch loads

### 2.4.5 Slowly Changing Dimensions (SCD)
- **SCD Type 1** — overwrite (no history)
- **SCD Type 2** — add new row with `valid_from`, `valid_to`, `is_current` ← most common
- **SCD Type 3** — add `previous_value` column (limited history)

### 2.4.6 Data Quality Framework (Great Expectations / Deequ)
- **Completeness** — not null, non-empty
- **Uniqueness** — deduplication checks on primary keys
- **Validity** — value in allowed domain (e.g., amount > 0)
- **Consistency** — cross-table referential integrity
- **Timeliness** — max latency from event time to availability
- **AWS Deequ** — open-source quality framework built on Spark (Capital One-adjacent)

---

## 💳 TOPIC 2.5: Capital One Fintech Context

### 2.5.1 PII / Sensitive Data (CRITICAL at Capital One)
- **PII** — Personally Identifiable Information: SSN, DOB, card number, name+address combination
- **Tokenization** — replace PAN (Primary Account Number) with non-sensitive token (Visa/Mastercard)
- **Masking** — show only last 4 digits of card
- **Encryption at Rest** — AES-256 (S3 SSE-KMS, Redshift encryption)
- **Encryption in Transit** — TLS 1.2+ for all API/data movement
- **Data Classification** — Public, Internal, Confidential, Restricted

### 2.5.2 Compliance Frameworks
- **PCI DSS** — Payment Card Industry Data Security Standard (mandatory for card data)
- **SOX** — Sarbanes-Oxley (financial data audit trails)
- **CCPA** / **GDPR** — consumer data rights (right to delete, right to access)
- **GLBA** — Gramm-Leach-Bliley Act (financial privacy)
- **Data Lineage** — tracking where data came from and how it transformed (Apache Atlas, OpenLineage)

### 2.5.3 Financial Metrics (Case Interview Prep)
- **CAC** (Customer Acquisition Cost)
- **LTV** (Customer Lifetime Value)
- **Charge-off Rate** — % of loans written off as uncollectible
- **Net Interest Margin (NIM)** — spread between borrowing and lending rates
- **Default Rates / Delinquency Rates**

### 2.5.4 Capital One's Tech Stack (Real Context)
- **100% AWS** — first major US bank to go all-in on cloud (pioneered 2012–2020)
- **Apache Spark** on EMR / Glue for large-scale batch
- **Apache Kafka / MSK** for event streaming
- **Apache Airflow / MWAA** for orchestration
- **Snowflake + Redshift** coexistence (team-dependent)
- **Terraform** for infrastructure-as-code
- **Python** as primary data engineering language
- Strong internal ML platform for credit decisioning

---

## 🎙️ TOPIC 2.6: Behavioral / STAR Framework (Power Day)

### 2.6.1 Capital One Leadership Principles
- **Customer Obsession** — decisions driven by customer impact
- **Do the Right Thing** — integrity, especially important in fintech
- **Excellence** — high-quality deliverables, continuous improvement
- **One Team** — cross-functional collaboration
- **Innovation** — challenge the status quo

### 2.6.2 STAR Method
- **Situation** — context and scale (use numbers!)
- **Task** — your specific responsibility
- **Action** — concrete steps YOU took (not the team)
- **Result** — measurable outcome (% improvement, $saved, time reduced)

### 2.6.3 Must-Prep STAR Stories for Lead DE
- Led a data pipeline migration / modernization
- Reduced data latency or processing time significantly
- Resolved a data quality crisis in production
- Mentored junior engineers / drove team standards
- Made a difficult technical trade-off with limited information
- Pushed back on requirements that violated data principles

---

# APPENDIX: PYTHON QUICK-REFERENCE CHEAT SHEET

```python
# ════════════════════════════════════════════════════
# COLLECTIONS ARSENAL
# ════════════════════════════════════════════════════
from collections import Counter, defaultdict, deque

freq = Counter(arr)                    # {val: count}
freq.most_common(k)                    # Top-k elements
adj = defaultdict(list)               # Graph adjacency list
q = deque([start])                    # BFS queue (O(1) popleft)
q.popleft()                           # NOT list.pop(0) — that's O(n)!

# ════════════════════════════════════════════════════
# HEAP (PRIORITY QUEUE)
# ════════════════════════════════════════════════════
import heapq
heapq.heapify(arr)                    # In-place, O(n)
heapq.heappush(heap, val)
heapq.heappop(heap)                   # Min element
heapq.heappush(heap, -val)            # Max-heap trick
heapq.nlargest(k, arr)               # Top-k largest
heapq.nsmallest(k, arr)              # Top-k smallest

# ════════════════════════════════════════════════════
# SORTING
# ════════════════════════════════════════════════════
arr.sort()                            # In-place, stable, Timsort
arr.sort(key=lambda x: (x[0], -x[1])) # Multi-key
sorted(arr, reverse=True)            # New list

# ════════════════════════════════════════════════════
# BINARY SEARCH
# ════════════════════════════════════════════════════
import bisect
bisect.bisect_left(arr, x)           # First index where arr[i] >= x
bisect.bisect_right(arr, x)          # First index where arr[i] > x
bisect.insort(arr, x)                # Insert maintaining order

# ════════════════════════════════════════════════════
# MEMOIZATION (TOP-DOWN DP)
# ════════════════════════════════════════════════════
from functools import cache

@cache
def dp(i: int, j: int) -> int:
    if base_case: return 0
    return min(dp(i+1, j), dp(i, j+1)) + cost[i][j]

# ════════════════════════════════════════════════════
# BFS TEMPLATE
# ════════════════════════════════════════════════════
from collections import deque

def bfs(grid: list[list[int]], sr: int, sc: int) -> int:
    m, n = len(grid), len(grid[0])
    q = deque([(sr, sc, 0)])         # (row, col, distance)
    visited = {(sr, sc)}
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        r, c, dist = q.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, dist+1))
    return -1

# ════════════════════════════════════════════════════
# MONOTONIC STACK TEMPLATE
# ════════════════════════════════════════════════════
def next_greater(arr: list[int]) -> list[int]:
    n = len(arr)
    result = [-1] * n
    stack: list[int] = []            # Stores indices
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

# ════════════════════════════════════════════════════
# UNION-FIND (DSU)
# ════════════════════════════════════════════════════
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True

# ════════════════════════════════════════════════════
# EDGE CASE CHECKLIST (Before Every Submit)
# ════════════════════════════════════════════════════
# [ ] Empty input:   if not arr: return 0
# [ ] Single element: if len(arr) == 1: return arr[0]
# [ ] All same values
# [ ] Negative numbers / zeros
# [ ] Maximum constraint (will O(n²) TLE?)
# [ ] Integer overflow? (Python int is arbitrary precision — no overflow)
# [ ] Off-by-one in loops, binary search bounds
```

---

# 🗓️ 10-DAY SPRINT SCHEDULE (Feb 13–23)

| Day | Morning (2 hrs) | Afternoon (2 hrs) | Evening (1 hr) |
|-----|----------------|-------------------|----------------|
| **Day 1 (Today)** | Phase A: Arrays, Prefix Sums, Hashing | LeetCode: 1, 217, 560, 974 | Review solutions |
| **Day 2** | Phase A: Strings + Simulation (OOP) | LeetCode: 2043 (Bank), 937, 49, 242 | CodeSignal Arcade warm-up |
| **Day 3** | Phase B: Two Pointers + Sliding Window | LeetCode: 11, 3, 76, 15 | 30-min timed mini-mock |
| **Day 4** | Phase B: Sorting + Intervals + Greedy | LeetCode: 56, 875, 347, 739 | Review edge cases |
| **Day 5** | Phase C: Matrix Traversal + Rotation | LeetCode: 54, 48, 73 | Spiral Matrix drill |
| **Day 6** | Phase C: BFS/DFS on Grid | LeetCode: 200, 994, 79, 695 | 30-min BFS timed drill |
| **Day 7** | Phase D: Dynamic Programming 1D | LeetCode: 198, 322, 300, 152 | DP pattern review |
| **Day 8** | Phase D: Monotonic Stack + Binary Search on Answer | LeetCode: 84, 42, 1011 | Full 70-min mock #1 |
| **Day 9** | Full 70-min mock #2 + review | Full 70-min mock #3 (simulate real conditions) | Debrief + weak spots |
| **Day 10** | Light review of weak areas | Rest — no new problems | Logistics: ID, camera, browser, room check; test proctoring setup |

---

# ✅ MASTER SUCCESS CHECKLIST

**CodeSignal Ready:**
- [ ] Solve LeetCode 2043 (Simple Bank System) in < 15 min
- [ ] Solve LeetCode 54 (Spiral Matrix) without off-by-one errors
- [ ] Solve LeetCode 84 (Largest Rectangle) with monotonic stack
- [ ] Identify "Sliding Window" pattern in < 30 seconds of reading
- [ ] Can write BFS template from memory in < 3 min
- [ ] Always test: empty input, single element, max constraints

**Power Day Ready:**
- [ ] Can write a window function query with PARTITION BY / ORDER BY / frame clause
- [ ] Explain broadcast join vs sort-merge join trade-offs
- [ ] Can design a fraud detection pipeline end-to-end (Kafka → Flink → DynamoDB → S3)
- [ ] Know PCI DSS basics and PII handling at Capital One
- [ ] Have 5+ STAR stories ready with measurable outcomes
- [ ] Understand Capital One's AWS-first architecture

---

*Compiled from: Glassdoor candidate reports 2024–2026, Prepfully staff engineer feedback (Nov 2024), Blind community threads, CodeSignal official documentation, InterviewQuery Capital One guide, Grok/Gemini/Claude AI roadmaps, and all uploaded reference materials.*
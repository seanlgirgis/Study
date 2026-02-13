Here's a structured **roadmap of topics and subtopics** for preparing for the Capital One Lead Data Engineer CodeSignal assessment (based on recent candidate reports from 2024–2026, CodeSignal's General Coding Assessment / GCA pattern, and typical patterns seen for engineering roles at Capital One).

This focuses purely on the **70-minute, 4-question Python coding challenge** — usually algorithmic / data-structure heavy rather than pure SQL or Spark (those tend to come later in Power Day). The goal is production-grade, efficient, readable Python code that handles edge cases well.

### 1. Core Easy / Warm-up Patterns (Q1 & often Q2 – aim to solve in 10–20 min total)
   - Array / List Manipulation
     - Traversal & neighbor comparisons
     - Prefix/suffix sums or running totals
     - Filtering / counting elements with conditions
     - Alternating patterns (parity, signs, etc.)
   - String Processing Basics
     - Character frequency / counting
     - Substring search or pattern matching
     - String splitting / joining / replacement rounds
     - Anagrams / similar pairs detection
   - Hashing Fundamentals
     - Dictionaries / Counters for frequency
     - Two-sum / pair finding variants
     - Grouping elements by key

### 2. Medium Patterns – Need Clean & Optimal (Q2 or Q4 – usually 15–25 min each)
   - Two Pointers & Sliding Window
     - Sorted arrays → two pointers
     - Variable-size window for subarrays/substrings
     - Fixed-size window problems
   - Sorting & Custom Comparators
     - Sorting with keys / multiple criteria
     - Interval merging / overlapping
   - HashMap + Sorting Combinations
     - Top K / most frequent elements
     - Group anagrams / similar items
   - Greedy Algorithms (light)
     - Interval scheduling
     - Activity selection style

### 3. Matrix / 2D Grid Patterns (Very common Q3 – often time sink, many partial / skip)
   - Matrix Traversal
     - Spiral order traversal
     - Row / column wise processing
     - Diagonal traversals
   - DFS / BFS on Grid
     - Flood fill / connected components
     - Number of islands variants
     - Shortest path in grid (basic BFS)
   - Matrix Rotation / Transformation
     - In-place rotation (90 degrees)
     - Transpose + reverse tricks
   - Dynamic Programming on 2D
     - Path finding with constraints (min cost path, unique paths)
     - DP table filling row-by-row

### 4. Hard / Optimization Patterns (Q3 or Q4 – aim for partial credit or full if time allows)
   - Dynamic Programming (1D & state-based)
     - Classic 1D DP (house robber, climbing stairs variants)
     - Subarray / subsequence problems (longest increasing, max product)
     - Knapsack style or partitioning
   - Advanced Two Pointers / Binary Search
     - Binary search on answer (min-max problems)
     - Median of two sorted arrays style logic
   - Monotonic Stack / Queue
     - Next greater / smaller element
     - Largest rectangle in histogram variants
     - Trapping rain water style
   - Graph Basics (sometimes appears)
     - BFS on implicit graph (grid or array-based)
     - Cycle detection light
     - Connected components

### 5. Cross-Cutting Skills (Apply to Every Question)
   - Edge Cases & Robustness
     - Empty inputs, single element, all same values
     - Negative numbers, zeros, large values
     - Out-of-bounds prevention
   - Time & Space Complexity Awareness
     - O(n) vs O(n log n) vs O(n²) trade-offs
     - In-place where possible
   - Clean Python Code Style
     - Type hints (List[int], Dict[str, int], etc.)
     - List/dict comprehensions vs loops
     - collections (Counter, defaultdict, deque)
     - Early returns for invalid cases

### Suggested Practice Priority Order (MVP-first for the sprint)
1. Arrays + Hashing + Two Pointers (80% of Q1/Q2 success)
2. Sliding Window + Sorting applications
3. Matrix / Grid traversal + DFS/BFS variants (decide fast if worth full attempt)
4. 1D DP + Monotonic stack (high ROI for partial on Q4)
5. Greedy + Binary Search on answer (frequent in harder Q4)

This structure matches the most consistent recent feedback: Q1/Q2 → solvable with good fundamentals; Q3 → frequently matrix/grid heavy; Q4 → optimization / DP / monotonic often.

We can start drilling Day 1 with 1–2 from the top buckets (arrays/hashing/two pointers) → propose a problem skeleton → I implement/test/refine → review timing & edge cases → log to solutions/ folder.

Sound good? Let me know your self-assessed comfort zones so we can weight the first session.

The current date is February 13, 2026 → 10 days left until the Feb 23 deadline. That's tight but realistic for a focused sprint if we go hard on high-ROI patterns and timed mocks.

Reassessing the plan from zero (ground truth from recent 2025–early 2026 reports across Reddit, Glassdoor, Blind, Prepfully, etc.):

### Key Reality Check from Recent Experiences (Capital One CodeSignal for Data Engineer / Lead / Senior / Software roles)
- **Format unchanged**: 70 minutes, 4 questions, proctored, Python allowed (and preferred for DE roles).
- **Difficulty curve**: Q1 easy (array/string/hash basics), Q2 easy-medium, Q3 frequently matrix/2D grid heavy (DFS/BFS/flood-fill/spiral/rotation — often the biggest time sink; many candidates get partial or skip), Q4 medium-hard (DP, monotonic stack/queue, graph BFS variants, binary search on answer, or greedy optimization).
- **Scoring reality**: Aim for ~500–760+ to advance (solve 3 fully + partial on 4th is common passing threshold; 3/4 full often enough for DE roles).
- **DE specificity**: Still pure algorithmic/DSA (LeetCode-style) — **not** heavy SQL, PySpark, pandas data wrangling, or ETL simulation in the CodeSignal round (those hit in Power Day technical/case study rounds). One 2025 report griped "for DE job, riddles had nothing to do with data" — confirms it's general coding assessment (GCA framework).
- **Common patterns 2025–2026**:
  - Matrix/grid traversal or search (Q3 staple — "tough matrix", "medium Graph BFS on grid").
  - Variations of Largest Rectangle in Histogram / monotonic stack.
  - Standard array/string/hash easy starters.
  - DP or optimization for Q4.
- **Strategy winners**: Solve Q1 → Q2 → Q4 first (skip/partial Q3 if time <15 min left). Many passers did exactly this.

### Reassessed Roadmap – Zero to True Hero (Prioritized for 10-Day Sprint)
Refined buckets with **2025–2026 emphasis** (matrix Q3 risk, Q4 optimization push). Order = daily practice priority.

1. **Foundation Warm-ups – Nail in <15 min total (Q1 + start of Q2)**
   - Array traversal, prefix sums, counting / frequency
   - String char freq, anagrams, substring basics
   - Hashing: Counter, dict grouping, two-sum variants

2. **Medium Bread-and-Butter – Must full-solve fast (Q2 & often Q4)**
   - Two pointers (sorted arrays, remove duplicates, container with most water style)
   - Sliding window (variable & fixed size — subarray sums, longest substring)
   - Sorting + custom key / interval problems (merge intervals, meeting rooms)
   - Greedy light (jump game variants, task scheduling)

3. **Matrix / Grid Heavy – Decide fast: full attempt or partial + move on (Q3 killer)**
   - 2D traversal: row/col/diagonal/spiral order
   - DFS/BFS flood fill, connected components, number of islands variants
   - Matrix in-place ops: transpose, rotate 90°, zero matrix set
   - Basic grid shortest path (BFS)

4. **Hard / Scoring Differentiators – Partial credit gold (Q4 or tough Q3)**
   - 1D DP: house robber, max subarray variants, climb stairs / partition
   - Monotonic stack/queue: next greater element, trapping rain water, largest rectangle histogram
   - Binary search on answer (min-max load, capacity to ship packages)
   - Graph lite: implicit graph BFS (often grid-based), cycle detection basics

5. **Cross-Cutting Mastery – Every solution**
   - Edge-case paranoia: [], [single], negatives/zeros, duplicates, large inputs
   - Python production-grade: type hints (List[int], etc.), collections (Counter, deque, defaultdict), early returns, O(n) preference
   - Time awareness: if >20 min on one problem → note partial, jump ahead

### Adjusted Sprint Workflow (MVP – 10 days to Feb 23)
- **Days 1–3**: Heavy on 1 + 2 (arrays/hashing/two pointers/sliding window/sorting). 2–3 LeetCode-style problems/day + 1 timed 30-min mini-mock.
- **Days 4–6**: Matrix/grid focus (bucket 3) — practice "skip or partial" decision. Add 1 full 70-min mock every 2 days.
- **Days 7–9**: Hard patterns (bucket 4) + mixed timed mocks (3–4 full 70-min sessions). Simulate: start Q1/Q2/Q4 first.
- **Day 10**: Light review + 1 final mock. Rest / tech check (camera/mic/ID/browser).
- **Artifact capture**: After each session → pseudo-file notes like:
  - solutions/2026-02-13-mock-01/q3-grid-bfs.py (code + timing: "12 min partial, BFS visited set key")
  - Teachables/150001-matrix-decision-tree.md ("when to abandon Q3: <3 directions explored in 18 min")
  - decisions.md entry: "2026-02-14: Q-order strategy confirmed — prioritize non-matrix"

This gets us to consistent 3/4 full solves + partial hard one → passing likelihood high.

Your comfort levels? (E.g., "strong arrays/hashing, medium sliding window, weak matrix/DP"?) Tell me so Day 1 targets hit your gaps first.

Ready to kick off with a sample problem from bucket 1–2? Or tweak this reassessment? Let's lock the charter and start building artifacts.
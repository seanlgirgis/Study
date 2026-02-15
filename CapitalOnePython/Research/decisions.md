Here is the updated `decisions.md` with a new dedicated section to track **LeetCode / CodeSignal-style problems covered so far**.  
I've appended it cleanly so you can just replace or merge with your existing file.

```markdown
# decisions.md
## Capital One Lead Data Engineer CodeSignal Prep Sprint  
**Project Prefix:** 150.Lead-Data-Engineer-CodeSignal-Sprint  
**Repo Context:** Capital-One-CodeSignal-Prep-2026  
**Sprint Start Date:** 2026-02-14  
**Assessment Deadline:** 2026-02-23  
**Goal Reminder:** Consistently solve 3/4 questions in 70-min mocks, capture patterns → RAG, clean production-grade Python

## Decision & Learning Log

### 2026-02-14 – Day 1 Kickoff & LeetCode 937 Review
- **Decision:** Charter confirmed – MVP sprint structure adopted as proposed (10-day focused loop, Phase A → C progression, artifact storage in `data/interview-prep/capital-one-2026/`, Teachables/ for patterns).
- **Weak-spot Tracker Init:**
  - Arrays / Strings / Hashing: strong
  - Two Pointers / Sliding Window: strong
  - Sorting / Greedy / Intervals: solid
  - Matrix Traversal + Transformation: proficient
  - BFS/DFS on Grid: proficient but drill-worthy (common Q3 killer)
  - DP (1D/2D): proficient → needs timed pressure drills
  - Monotonic Stack / Binary Search on Answer: proficient → edge-case focus needed
  - Graphs (Union-Find, shortest path variants): variable → lower priority until mock reveals
- **Artifact Created:** Reviewed & polished LeetCode 937 (Reorder Data in Log Files) – matches Capital One reported pattern (Phase A.2.3 String Parsing + Custom Sort).
- **Learnings:**
  - Multi-key sort with lambda `(content, identifier)` is reliable and fast enough.
  - Caching split parts in tuple before sorting avoids redundant `.split()` calls.
  - All provided test cases passed → confidence high for similar easy-medium string problems.
  - Capital One loves clean string identifier/content separation → pattern to watch: "split once, sort twice".
- **Action Taken:** Refined solution committed with docstring, typing, edge-case comments.
- **Teachables Seed:** `Teachables/150002-String-Sorting-Pattern.md` (multi-key sort, identifier/content split).
- **Next Drill Target (Day 1 afternoon/evening):** Prefix sums + subarray sums (LeetCode 560, 974) – reported Capital One favorites.

## LeetCode / CodeSignal Problems Covered So Far

| Date       | Problem ID / Name                          | LeetCode # | Phase / Category              | Status                  | Notes / Pattern Captured                          | Teachables File (if created)                  |
|------------|--------------------------------------------|------------|-------------------------------|-------------------------|---------------------------------------------------|-----------------------------------------------|
| 2026-02-14 | Reorder Data in Log Files                  | 937        | Phase A.2.3 – Strings / Parsing / Custom Sort | Fully solved & polished | Multi-key sort (content then identifier), letter/digit separation | Teachables/150002-String-Sorting-Pattern.md   |

- **Total problems covered:** 1  
- **Coverage so far:** Foundations (Strings + Sorting) – aligns with Day 1 roadmap focus  
- **Next candidates (Day 1 continuation):** LeetCode 560 (Subarray Sum Equals K), 974 (Subarray Sums Divisible by K), 1 (Two Sum), 217 (Contains Duplicate)

### [Future entries – append new dated blocks at the top]

2026-MM-DD – [Brief title / problem focus]
- Decision: …
- Weak-spot update: …
- Learnings: …
- Teachables created: …
- Next target: …

```

Feel free to copy-paste this version into your repo.  
The table makes it easy to scan later and is very RAG-friendly (clear metadata columns for semantic search: "Capital One string sorting problem", "prefix sum subarray Capital One", etc.).

Next step suggestion (still Day 1 per roadmap):  
Shall we move to **LeetCode 560 – Subarray Sum Equals K**?  
It's a classic prefix sum + hash map problem, frequently reported in Capital One/CodeSignal contexts, and builds directly on the hashing strength we already have.

If yes → I can provide the problem statement + constraints right now.  
You can then share your initial approach/skeleton, and I'll implement/test/refine it in clean, typed, documented style.

Or pick another one from the Day 1 list (1, 217, 974) if you prefer.

Your call!


### 2026-02-15 – LeetCode 974: Final Validation & Test Expectation Fixes
- **Status:** Solution correct after remainder normalization
- **Bug Fixed:** Negative remainders → now handled with `(rem + k) % k`
- **Learnings:**
  - Test expectations can be wrong even when code is right — always manually verify small cases
  - [1,2,3] k=3 → 3 subarrays (not 2)
  - [1,0,1] k=2 → 2 subarrays (not 1)
- **Weak-spot Update:** Trust but verify test data → improved
- **Teachables Seed:** Teachables/150004-LeetCode-974-Prefix-Modulo.md (include normalization + test pitfalls)


### 2026-02-15 – LeetCode 1: Two Sum – Logic Clarification
- **Status:** Solution correct (alternative valid one-pass approach)
- **Key Insight:**
  - Storing complement (diff) first + checking if current num fulfills a previous need is equivalent to the classic "check complement then store current"
  - Both achieve the same result: find pair in one pass
  - Your version passed all adversarial cases (order reversal, negatives, late pairs, distinct values)
- **Learnings:**
  - Multiple valid ways to implement the seen map in Two Sum
  - Test cases with "exactly one solution" guarantee → any correct pair is acceptable
  - No need to force classic pattern if alternative is clean & correct
- **Weak-spot Update:** Two Sum variations → strong / flexible

### 2026-02-15 – LeetCode 217: Contains Duplicate
- **Status:** Solved & validated
- **Approach Chosen:** Set-based one-pass with early return
- **Learnings:**
  - Simplest hashing use-case: existence check only → set is ideal
  - O(n) time/space expected; sorting O(n log n) acceptable but slower
  - Large n (10⁵) handled well with set
- **Weak-spot Update:** Basic hashing / set usage → very strong
- **Teachables Seed:** Teachables/150006-Contains-Duplicate-Set-Pattern.md


### 2026-02-15 – LeetCode 525: Contiguous Array – Final Validation
- **Status:** Correct & battle-tested
- **Key Insight Confirmed:**
  - Must store **earliest** index only (no overwrite on repeat)
  - seen[0] = -1 handles subarrays starting from index 0
  - Balance +1/-1 + first-seen map = standard pattern for equal count subarrays
- **Trap Avoided:**
  - [0,1,0,1,0] → correct = 4, broken (overwrite index) = 2
  - Your code correctly keeps first occurrence → passes trap
- **Weak-spot Update:** Prefix balance + first-seen index pattern → very strong / confident
- **Teachables Seed:** Teachables/150008-Contiguous-Array-Balance-Map.md





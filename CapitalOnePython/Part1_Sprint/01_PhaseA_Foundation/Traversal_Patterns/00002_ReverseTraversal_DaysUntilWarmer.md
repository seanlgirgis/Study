Linear scan is solid — one problem is enough for that pattern. Let me design the reverse traversal exercise.
Leetcode 739
---

**Project: Capital-One-CodeSignal-Prep-2026**
**Sprint: 150.Lead-Data-Engineer-CodeSignal-Sprint**
**Date: February 13, 2026**
**Session: Day 1 — Phase A.1.2 Traversal Patterns**

---

### A.1.2 Traversal Patterns — Focus today
Reverse traversal using `range(n-1, -1, -1)`
→ You scan the array **backwards**, from the last element to the first.
→ Key insight: sometimes the answer depends on **what comes after** the current element, not before. Reverse traversal lets you carry that information forward as you scan.

Common flavors seen in Capital One / CodeSignal style:
- Find the last occurrence of something
- Compare each element to what comes **after** it
- Build a result array from right to left
- Carry a running state backwards through the array

---

### Practice Problem — Test-style version

**Problem: Days Until Warmer**

Given a list of daily temperatures `temps`, return a list `result` where `result[i]` is the number of days you have to wait after day `i` to get a warmer temperature.

If there is no future day with a warmer temperature, `result[i]` should be `0`.

**Example 1:**
Input: `temps = [73, 74, 75, 71, 69, 72, 76, 73]`
Output: `[1, 1, 4, 2, 1, 1, 0, 0]`
Explanation:
- Day 0 (73°): next warmer is day 1 (74°) → 1 day
- Day 2 (75°): next warmer is day 6 (76°) → 4 days
- Day 6 (76°): no warmer day after → 0
- Day 7 (73°): no warmer day after → 0

**Example 2:**
Input: `temps = [30, 40, 50, 60]`
Output: `[1, 1, 1, 0]`
Explanation: Each day is warmer than the last. Last day has no future day.

**Example 3:**
Input: `temps = [30, 20, 10]`
Output: `[0, 0, 0]`
Explanation: Strictly decreasing — no day has a warmer future day.

**Example 4:**
Input: `temps = [50]`
Output: `[0]`

**Example 5:**
Input: `temps = []`
Output: `[]`

**Constraints:**
- `0 ≤ temps.length ≤ 10⁴`
- `0 ≤ temps[i] ≤ 100`

**Your task:**
Write a function in Python that solves this.

```python
from typing import List


class Solution:
    def daysUntilWarmer(self, temps: List[int]) -> List[int]:
        # Your code here
        pass
```

---

### Instructions for you (simulate real test conditions)
1. Time yourself — aim for **under 12 minutes**
2. Do **not** look up anything — pretend it's proctored
3. Handle all edge cases first
4. Write clean code with:
   - Type hints
   - Docstring (brief)
   - Early returns for empty / trivial cases
5. Use **reverse traversal** — `range(n-1, -1, -1)` — do not use a stack

---

### Hint (only read if stuck after 8 minutes)
<details>
<summary>Click to reveal</summary>

Start from the last day and work backwards. For each day `i`, you already know the answers for every day to the right of `i`. Use that to jump forward efficiently instead of scanning every future day one by one.

</details>

---

Start your timer — go!

# Cheat Sheet #5: Expert Optimization & Strategy

**Focus**: DP, monotonic structures, binary search on answer, Union-Find + test-day playbook.  
**Target**: Differentiate on Q4 hard + partial credit on Q3 killer; consistent 3/4 full solves.  
**Alignment**: Roadmap Phase D (DP / Monotonic Stack / Binary Search) + Phase F (Strategy).  
**Mindset**: When stuck → fall back to brute → optimize step-by-step. Always submit partial.

## 1. Dynamic Programming (1D / 2D)

**Top-Down Memoization (cleanest for most problems)**
```python
from functools import cache
from typing import List

@cache
def rob_memo(nums: List[int], i: int = 0) -> int:
    """House Robber – max loot without adjacent houses."""
    if i >= len(nums):
        return 0
    return max(
        nums[i] + rob_memo(nums, i + 2),   # rob this house
        rob_memo(nums, i + 1)              # skip this house
    )

# Usage: rob_memo(tuple(nums))  # tuple for hashable cache
```

**Bottom-Up Tabulation (space-optimized 1D)**
```python
def rob_tab(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2, prev1 = 0, nums[0]
    for i in range(1, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    return prev1
```

**Common 1D DP Patterns**
- House Robber (LC 198)
- Coin Change (LC 322)
- Longest Increasing Subsequence (LC 300 – O(n log n) with patience sorting)

**2D DP Example (Grid Path)**
```python
@cache
def min_path(grid: List[List[int]], i: int, j: int) -> int:
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return grid[i][j]
    if i >= len(grid) or j >= len(grid[0]):
        return float('inf')
    return grid[i][j] + min(
        min_path(grid, i + 1, j),
        min_path(grid, i, j + 1)
    )
```

## 2. Monotonic Stack / Deque

**Next Greater Element (classic stack template)**
```python
def next_greater_elements(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [-1] * n
    stack: List[int] = []  # indices
    
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    # For circular: run twice or double the array
    return result
```

**Trapping Rain Water (LC 42)**
```python
def trap(height: List[int]) -> int:
    if len(height) < 3:
        return 0
    
    left_max = right_max = water = 0
    left, right = 0, len(height) - 1
    
    while left < right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
```

**Monotonic Deque for Sliding Window Maximum (LC 239)**
Use deque to keep indices in decreasing order of values.

## 3. Binary Search Variants

**Standard bisect**
```python
import bisect

# Find insertion point
idx = bisect.bisect_left(sorted_arr, target)   # first >= target
idx = bisect.bisect_right(sorted_arr, target)  # first > target
```

**Binary Search on Answer (very common hard)**
```python
def ship_within_days(weights: List[int], days: int) -> int:
    def can_ship(capacity: int) -> bool:
        current = days_left = 0
        for w in weights:
            if current + w > capacity:
                days_left += 1
                current = w
                if days_left > days:
                    return False
            else:
                current += w
        return True
    
    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

## 4. Union-Find (Disjoint Set Union – DSU)

**Path-compressed + union-by-rank template**
```python
class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True
```

**Use case**: Number of connected components, cycle detection, Kruskal MST.

## 5. Test-Day Strategy & Execution

**Question Order (confirmed winning strategy)**
1. Q1 (easy) → solve <10 min
2. Q2 (easy-medium) → solve <15 min
3. Q4 (medium-hard) → solve or strong partial
4. Q3 (matrix/grid killer) → partial credit or brute if time

**Partial Credit Rule**: Submit something — even brute force gets points (post-2023 scoring).

**Time Allocation (70 min total)**
- 0–10 min: Q1
- 10–25 min: Q2
- 25–50 min: Q4
- 50–70 min: Q3 (or polish previous)

**Before Submit Checklist**
- Empty input? Single element? All same? Negatives/zeros?
- Off-by-one in loops/indexes?
- O(n²) on n=10^5 → TLE risk?
- Mutable default args in functions?
- Visited set / bounds check in grid?

**Proctoring Reminders**
- Quiet room, no one enters frame
- ID ready, good lighting
- Chrome/Firefox, stable internet
- No notes, no AI — screen + cam + mic recorded

---

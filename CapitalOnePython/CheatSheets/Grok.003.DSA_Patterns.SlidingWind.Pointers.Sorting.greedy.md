
# Cheat Sheet #3: Intermediate DSA Patterns (Two Pointers, Sliding Window, Sorting, Greedy Basics)

**Focus**: Core optimization patterns for Q2 (easy-medium) and parts of Q4.  
**Target**: Solve medium problems cleanly in <15–20 min; recognize pattern in <30 seconds.  
**Alignment**: Roadmap Phase B (Two Pointers, Sliding Window, Sorting, Greedy).  
**Key Mindset**: Always ask: "Can I avoid O(n²)? → two pointers / window / sort + linear pass".

## 1. Two Pointers

### Opposite-End Pointers (Sorted Arrays / Squeeze)
Classic for sum / container / partition problems.

**Template**
```python
from typing import List

def two_pointers_example(nums: List[int], target: int) -> List[int]:
    """Find two numbers that sum to target (sorted input)."""
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

**High-Frequency Problems**
- LC 167 – Two Sum II (sorted)
- LC 11 – Container With Most Water (max area = min(height) × width)
- LC 15 – 3Sum (sort + two pointers inside loop)

**Edge Cases**
- Duplicates (skip or handle)
- All negative / zero
- No solution → return []

### Same-Direction Pointers (Fast/Slow)
Used for cycle detection, remove duplicates in-place.

**Template – Remove Duplicates from Sorted Array**
```python
def remove_duplicates(nums: List[int]) -> int:
    """Return length after removing duplicates in-place."""
    if not nums:
        return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

**Common Use**: LC 26 (Remove Duplicates), LC 141 (Linked List Cycle – Floyd’s)

## 2. Sliding Window

### Fixed-Size Window
Maintain sum / max / min over k elements.

**Template – Max Average Subarray**
```python
def find_max_average(nums: List[int], k: int) -> float:
    """Maximum average of any contiguous subarray of size k."""
    if len(nums) < k:
        return 0.0
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k
```

### Variable-Size Window (Expand → Contract)
Most powerful — longest / shortest / at-most-k.

**Template – Longest Substring Without Repeating Characters**
```python
from collections import defaultdict

def length_of_longest_substring(s: str) -> int:
    """Longest substring without repeating characters."""
    if not s:
        return 0
    char_index = {}
    left = max_length = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
```

**Alternative with Counter / Set**
```python
from collections import Counter

def length_of_longest_substring_counter(s: str) -> int:
    count = Counter()
    left = max_len = 0
    for right, char in enumerate(s):
        count[char] += 1
        while count[char] > 1:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

### "At Most K" Pattern (Variable Window)
Generic template for "longest subarray with at most K zeros/distinct chars/etc".

```python
def at_most_k(nums: List[int], k: int) -> int:
    left = 0
    res = 0
    for right in range(len(nums)):
        # 1. Expand (add nums[right])
        # ... update state ...
        
        # 2. Contract (while state invalid > k)
        while state > k:
            # ... remove nums[left] ...
            left += 1
            
        # 3. Update result (window is valid)
        res = max(res, right - left + 1)
    return res
```

**High-Frequency Problems**
- LC 3 – Longest Substring Without Repeating Characters ★
- LC 424 – Longest Repeating Character Replacement
- LC 76 – Minimum Window Substring (harder, but pattern same)

**Edge Cases**
- All unique → whole string
- All same → length 1 (or k)
- Empty / single char
- Window shrinks past left

## 3. Sorting & Custom Comparators

**Built-in**
```python
arr.sort()                      # in-place
sorted_arr = sorted(arr)        # new list
arr.sort(reverse=True)
```

**Custom Key (Critical for Capital One)**
```python
# Sort by length then lexicographically
words = ["cat", "dog", "apple", "bat"]
words.sort(key=lambda x: (len(x), x))

# Multi-key: asc primary, desc secondary
points = [(1, 5), (1, 3), (2, 4)]
points.sort(key=lambda p: (p[0], -p[1]))
```

**Interval Problems – Merge Overlapping**
```python
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for curr in intervals[1:]:
        last = merged[-1]
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            merged.append(curr)
    return merged
```

**High-Frequency**
- LC 56 – Merge Intervals ★
- LC 252/253 – Meeting Rooms
- LC 435 – Non-overlapping Intervals (greedy sort by end)

## 4. Greedy Basics (Often Combined)
Choose local optimum → global optimum.

**Example Pattern**: Sort + pick earliest finish (activity selection)
- Sort intervals by end time
- Pick first → skip overlapping → repeat

**Quick Check**: Can I prove greedy choice property? (Often yes for intervals, scheduling)

**High-Frequency Greedy + Sort**
- LC 435 – Non-overlapping Intervals
- LC 55/45 – Jump Game variants (greedy max reach)

## Edge Cases Checklist (Before Submit)
- [] empty input
- [single] element
- All same values
- Negatives / zeros
- Already sorted / reverse sorted
- Maximum constraints (n ≤ 10^5 → O(n log n) ok, O(n²) risky)



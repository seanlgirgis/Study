# Cheat Sheet #2: Data Structures Fundamentals (Beginner-Intermediate)

**Focus**: Master mutable/immutable collections for frequency, lookups, grouping — foundation of Q1/Q2 problems.  
**Target**: Solve easy-medium array/string/hash problems in <15 min (e.g., Two Sum with dict, anagram check with Counter).  
**Alignment**: Roadmap Phase A (Arrays, Strings, Hashing) + collections arsenal.  
**Style**: Python 3.12, type hints, docstrings, edge-case robust.

## 1. Lists (Mutable, Ordered)
Ordered, indexable, changeable.

```python
from typing import List

nums: List[int] = [1, 2, 3, 4, 5]
print(nums[0])          # 1
print(nums[-1])         # 5
print(nums[1:4])        # [2, 3, 4]
print(nums[::-1])       # [5, 4, 3, 2, 1]  # reverse copy
```

**Modify Operations**
- `nums.append(6)` → [1,2,3,4,5,6]
- `nums.insert(0, 0)` → [0,1,2,3,4,5,6]
- `nums.extend([7,8])` → append multiple
- `nums.pop()` → remove & return last (default)
- `nums.pop(0)` → remove & return at index 0 (O(n)!)
- `nums.remove(3)` → remove first occurrence
- `del nums[1]` → delete by index

**Search & Sort**
- `nums.index(4)` → first index of 4 (ValueError if missing)
- `nums.count(2)` → number of 2's
- `nums.sort()` → in-place ascending
- `nums.sort(reverse=True)` → in-place descending
- `sorted_nums = sorted(nums)` → new sorted list
- `nums.reverse()` → in-place reverse

**List Comprehensions** (fast & readable)
```python
squares: List[int] = [x**2 for x in range(10)]          # [0,1,4,9,...,81]
evens: List[int] = [x for x in range(20) if x % 2 == 0] # [0,2,4,...,18]
flat = [x for row in matrix for x in row]               # flatten 2D list
```

**Edge Cases & Tips**
- Empty: `if not nums: return 0`
- Single element: `if len(nums) == 1: return nums[0]`
- Avoid `nums += [x]` in loop → quadratic. Use list + `.append()` or pre-allocate.
- `pop(0)` is O(n) — use `collections.deque` for fast pops from left.

**Exercise**: Remove all even numbers in-place.
```python
def remove_evens(nums: List[int]) -> None:
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            nums.pop(i)
        else:
            i += 1
```

## 2. Dictionaries (Mutable, Key-Value)
Fast lookups by key.

```python
from typing import Dict

d: Dict[str, int] = {"a": 1, "b": 2, "c": 3}
print(d["a"])           # 1
print(d.get("z", 0))    # 0 (safe default)
d["d"] = 4              # add/update
del d["a"]              # remove key
val = d.pop("b", None)  # remove & return (with default)
```

**Iteration**
```python
for k in d:               # keys only
for v in d.values():
for k, v in d.items():    # best: unpack key-value
    print(f"{k}: {v}")
```

**Dict Comprehension**
```python
freq: Dict[str, int] = {ch: s.count(ch) for ch in s}
inverted = {v: k for k, v in d.items() if v not in seen}  # careful with duplicates
```

## 3. collections — defaultdict & Counter (Your Best Friends)

```python
from collections import defaultdict, Counter

# defaultdict
dd = defaultdict(int)       # auto 0 on missing key
dd["apples"] += 1           # no KeyError

dd_list = defaultdict(list)
dd_list["key"].append(42)   # auto empty list

# Counter
cnt = Counter("aabbc")                  # Counter({'a':2, 'b':2, 'c':1})
print(cnt["z"])                         # 0 (missing = 0)
print(cnt.most_common(2))               # [('a',2), ('b',2)]
print(cnt.most_common())                # all, sorted descending
```

**Tip**: Use Counter for frequency → anagrams, top-k, grouping.  
Use defaultdict(list) for grouping by key (e.g., group anagrams).

## 4. Sets (Mutable, Unordered, Unique)
O(1) average lookups & deduplication.

```python
s = {1, 2, 3}
s.add(4)                # {1,2,3,4}
s.discard(2)            # safe remove (no error if missing)
# s.remove(5)           # KeyError if missing → prefer discard

# Operations
a = {1,2,3}; b = {2,3,4}
print(a | b)            # union {1,2,3,4}
print(a & b)            # intersection {2,3}
print(a - b)            # difference {1}
print(a ^ b)            # symmetric difference {1,4}
print(a.issubset(b))    # False
```

**Set Comprehension**
```python
unique_digits = {x % 10 for x in nums}
seen = set()            # fast membership: if x in seen
```

**Tip**: Convert list → set for dedup: `unique = list(set(nums))` (order not preserved).

## 5. Tuples (Immutable, Ordered)
Hashable → can be dict keys.

```python
t = (1, 2, 3)
a, b, c = t             # unpacking
a, *rest = t            # a=1, rest=[2,3]

# As dict keys
grid: Dict[tuple[int,int], str] = {}
grid[(0,0)] = "start"
```

**Named Tuples** (readable records)
```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)         # 3 4

## 7. Heaps (heapq) - Min-Heap by default
O(log n) push/pop. Essential for "Top K" or "Median".

```python
import heapq
min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 1)        # [1, 10]
smallest = heapq.heappop(min_heap) # 1

# Max-Heap? Multiply by -1 when pushing/popping.
# Heapify O(n):
nums = [3, 1, 4]
heapq.heapify(nums)                # nums is now a valid heap
```
```

## 6. Quick LeetCode Ties (Practice These Today)
- **LC 217 – Contains Duplicate**  
  Use set: `return len(nums) != len(set(nums))` — O(n) time/space.

- **LC 242 – Valid Anagram**  
  ```python
  from collections import Counter

  def isAnagram(s: str, t: str) -> bool:
      return Counter(s) == Counter(t)
  ```
  Alternative: sort → `sorted(s) == sorted(t)`

- **LC 1 – Two Sum** (hashmap version – faster than brute)
  ```python
  from typing import List, Dict

  def twoSum(nums: List[int], target: int) -> List[int]:
      seen: Dict[int, int] = {}
      for i, num in enumerate(nums):
          complement = target - num
          if complement in seen:
              return [seen[complement], i]
          seen[num] = i
      return []
  ```

**Edge Cases Checklist** (before submit)
- [] empty → []
- [1] single → handle or early return
- Duplicates allowed?
- Negative numbers / zero
- All same values

---

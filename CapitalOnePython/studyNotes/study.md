# 🐍 Python Learning Notes
> Single file. Add new notes at the TOP (newest first). Search with Ctrl+F.

---
## Quick Tag Index
- Basics: #basics
- Data Types: #types
- Functions: #functions
- OOP: #oop
- Algorithms: #algo
- Patterns: #pattern
- Gotchas: #gotcha
- AWS/Cloud: #aws

---

## [2025-02-17] - List Slicing Basics
**Category:** Data Types
**Tags:** #basics #types #list

A slice returns a NEW list, not a reference to the original.
```python
nums = [1, 2, 3, 4, 5]
chunk = nums[1:4]   # [2, 3, 4]
```

💡 Tip: Negative index counts from the end — nums[-1] is 5.
⚠️ Gotcha: Modifying chunk does NOT affect nums.

---

## [2025-02-15] - What is a Generator?
**Category:** Functions
**Tags:** #functions #memory #pattern

A generator yields values one at a time instead of building the whole list in memory.
```python
def count_up(n):
    for i in range(n):
        yield i
```

💡 Use when the list would be huge — saves memory.
⚠️ Gotcha: You can only iterate a generator ONCE.

---
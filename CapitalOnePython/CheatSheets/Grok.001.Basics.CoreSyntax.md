
# Cheat Sheet #1: Python Basics & Core Syntax (Newbie Level)

**Focus**: Absolute fundamentals to code quickly. Builds on your PDF (data types, operators, strings) with control flow, functions, exercises, pitfalls.  
**Why First?**: Ensures you read/write simple code before DSA (Roadmap Phase E).  
**Target**: Solve Q1 (easy array/string) in <10 min, like basic loops in LC 1 (Two Sum).  
**Tips**: Python 3.12+ dynamic typing — use `type(x)` or `isinstance(x, int)`. Indent with 4 spaces (black style). Run exercises in REPL for practice.

## 1. Data Types & Variables
Python is dynamically typed — no declarations needed. Use `=` for assignment.

| Type | Examples | Notes |
|------|----------|-------|
| int | `x = 10` <br> `y = -5` | Unlimited size; no overflow. |
| float | `pi = 3.14` <br> `e = 2.718` | Decimal precision; use `round(pi, 2)` → 3.14. |
| bool | `flag = True` <br> `done = False` | Capitalized! Truthy: non-zero/non-empty; Falsy: 0/None/empty. |
| str | `name = "Sean"` <br> `multi = """Line1\nLine2"""` | Immutable; single/double/triple quotes. |
| NoneType | `nothing = None` | Like null; check with `is None`. |

**Type Conversions**:
- `int("42")` → 42
- `float("3.14")` → 3.14
- `str(42)` → "42"
- `bool(0)` → False; `bool("hi")` → True

**Simple Exercise**: Convert user input to int and check if even.
```python
num_str = input("Enter a number: ")  # e.g., "10"
num = int(num_str)
print(num % 2 == 0)  # True
```

**Common Pitfalls**: Mixing types (e.g., "1" + 2 → TypeError). Fix: `int("1") + 2`. Off-by-one in ranges (see loops).

## 2. Operators
Use tables for categories (from your PDF).

| Category | Operators | Notes |
|----------|-----------|-------|
| Arithmetic | `+ - * / // % **` | `//` = floor div (7 // 2 = 3; -7 // 2 = -4). `**` = power (2**3=8). |
| Comparison | `== != < > <= >=` | Return bool. Strings compare lexically ("a" < "b"). |
| Logical | `and or not` | Short-circuit: `x and y` skips y if x False. |
| Bitwise | `& \| ^ ~ << >>` | `&` AND, `\|` OR, `^` XOR. E.g., 5 & 3 = 1 (101 & 011 = 001). |
| Identity | `is is not` | Same object? `[] is []` → False (different memory). |
| Membership | `in not in` | In str/list: "a" in "abc" → True. |
| Assignment | `+= -= *= //= **= %=` | Augmented: `x += 1`. |

**Tip**: `a / b` always float (3/2=1.5). For truncation toward zero: `int(a / b)`.

**Simple Exercise**: Check if number is positive and even.
```python
num = 4
print(num > 0 and num % 2 == 0)  # True
```

**Common Pitfalls**: Bitwise vs logical (`&` vs `and` — use logical for bools). Precedence: `2 + 3 * 4 = 14` (use parens for clarity).

## 3. Strings (Immutable)
Can't change in-place — ops return new strings.

- Indexing/Slicing: `s = "hello"`  
  `s[0]` → 'h'; `s[-1]` → 'o'  
  `s[1:4]` → 'ell'; `s[::-1]` → 'olleh' (reverse)  
  `len(s)` → 5

- Methods:  
  `s.split()` → ['hello', 'world'] (on space)  
  `s.split(',')` → split on delimiter  
  `' '.join(['a', 'b'])` → 'a b'  
  `s.strip()` → remove whitespace  
  `s.replace('o', '0')` → 'hell0'  
  `s.find('ll')` → 2 (-1 if not found)  
  `s.count('l')` → 2  
  `s.startswith('he')` → True  
  `s.upper()` / `s.lower()` / `s.title()`  
  `s.isdigit()` / `s.isalpha()` / `s.isalnum()`

- f-Strings: `f"{name} is {age}"` → "Sean is 30"  
  Formatting: `f"{3.14159:.2f}"` → "3.14"

**Simple Exercise**: Reverse a string and check palindrome.
```python
s = "radar"
print(s == s[::-1])  # True
```

**Common Pitfalls**: Mutating strings (`s[0] = 'H'` → TypeError). Build efficiently: Use list + join in loops (O(n) vs O(n²) with +=). Edge: Empty string `""` len=0.

## 4. Control Flow
Direct code flow.

- If/Else:  
  ```python
  x = 10
  if x > 0:
      print("Positive")
  elif x < 0:
      print("Negative")
  else:
      print("Zero")
  ```

- Loops:  
  For: `for i in range(5):` → 0-4 (start=0, stop=5, step=1)  
  `for char in "abc":` → 'a', 'b', 'c'  
  Enumerate (Preferred): `for i, val in enumerate(nums):` → get index AND value.  
  While:  
  ```python
  i = 0
  while i < 5:
      print(i)
      i += 1
  ```
  Break/Continue: `break` exits loop; `continue` skips to next iteration.

**Simple Exercise**: Sum numbers 1-10.
```python
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55
```

**Common Pitfalls**: Infinite loops (forget i+=1). Off-by-one: range(5) → 0-4, not 1-5. Indentation errors (SyntaxError).

## 5. Functions
Reusable code blocks.

- Define:  
  ```python
  def add(a: int, b: int) -> int:
      """Add two ints."""  # Docstring
      return a + b

  print(add(2, 3))  # 5
  ```

- Args: Defaults `def greet(name: str = "Sean"):`  
  Variable `*args` (tuple), `**kwargs` (dict).  

- Lambda: Anonymous: `double = lambda x: x*2` → double(3)=6.  
  Use for simple ops (e.g., sort keys later).

**Simple Exercise**: Function to check even.
```python
def is_even(n: int) -> bool:
    return n % 2 == 0

print(is_even(4))  # True
```

**Common Pitfalls**: No return → None. Mutable defaults (e.g., def foo(lst=[]):) — shares across calls (bad!). Use None + check.

## 6. Tips & Edge Cases
- Dynamic Typing: `isinstance(x, (int, float))` for checks.  
- Common Errors: Indentation (use 4 spaces), NameError (undefined var), IndexError (out of range).  
- Edge Cases: Empty inputs (`if not s:`), negatives/zeros, max values (Python ints handle big nums).  
- Best Practices: Type hints (mypy), docstrings, avoid globals.

## 7. LeetCode Ties
Start with basics: LC 1 (Two Sum) — use loops + if.
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # Edge: no solution
```
**Practice**: Time it <10 min. Brute O(n²) ok for newbie — optimize later.


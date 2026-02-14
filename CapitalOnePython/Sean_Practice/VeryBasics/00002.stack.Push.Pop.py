
from typing import List, Tuple

stack: List[Tuple[int, int]] = []

data = [73, 74, 75, 71, 69, 72, 76, 73]


# ─── PUSH ALL ITEMS ───────────────────────────────────────────
print("=" * 55)
print("PUSHING ITEMS ONTO THE STACK")
print("=" * 55)

for i, val in enumerate(data):
    stack.append((val, i))
    print(f"  Pushed {str((val, i)):<12} → Stack size: {len(stack)}")

print(f"\n  Final Stack (bottom → top):")
for i, item in enumerate(stack):
    label = " ← TOP" if i == len(stack) - 1 else ""
    label = " ← BOTTOM" if i == 0 else label
    print(f"    [{i}] {item}{label}")

# ─── POP FROM THE TOP ─────────────────────────────────────────
print("\n" + "=" * 55)
print("POPPING FROM THE TOP (LIFO)")
print("=" * 55)

for _ in range(3):
    item = stack.pop()
    print(f"  Popped {str(item):<12} → Stack size: {len(stack)}")

print(f"\n  Stack after top pops (bottom → top):")
for i, item in enumerate(stack):
    label = " ← TOP" if i == len(stack) - 1 else ""
    label = " ← BOTTOM" if i == 0 else label
    print(f"    [{i}] {item}{label}")

# ─── POP FROM THE MIDDLE ──────────────────────────────────────
print("\n" + "=" * 55)
print("POPPING FROM THE MIDDLE (index 2)")
print("=" * 55)

middle_index = 2
removed = stack.pop(middle_index)
print(f"  Popped {removed} from index [{middle_index}]")
print(f"  Stack size now: {len(stack)}")

print(f"\n  Stack after middle pop (bottom → top):")
for i, item in enumerate(stack):
    label = " ← TOP" if i == len(stack) - 1 else ""
    label = " ← BOTTOM" if i == 0 else label
    print(f"    [{i}] {item}{label}")

# ─── POP REMAINING ────────────────────────────────────────────
print("\n" + "=" * 55)
print("POPPING ALL REMAINING ITEMS")
print("=" * 55)

while stack:
    item = stack.pop()
    print(f"  Popped {str(item):<12} → Stack size: {len(stack)}")

print("\n  Stack is empty:", stack)
print("=" * 55)

"""
**Output:**
```
=======================================================
PUSHING ITEMS ONTO THE STACK
=======================================================
  Pushed (73, 0)      → Stack size: 1
  Pushed (74, 1)      → Stack size: 2
  Pushed (75, 2)      → Stack size: 3
  Pushed (71, 3)      → Stack size: 4
  Pushed (69, 4)      → Stack size: 5
  Pushed (72, 5)      → Stack size: 6
  Pushed (76, 6)      → Stack size: 7
  Pushed (73, 7)      → Stack size: 8

  Final Stack (bottom → top):
    [0] (73, 0) ← BOTTOM
    [1] (74, 1)
    [2] (75, 2)
    [3] (71, 3)
    [4] (69, 4)
    [5] (72, 5)
    [6] (76, 6)
    [7] (73, 7) ← TOP

=======================================================
POPPING FROM THE TOP (LIFO)
=======================================================
  Popped (73, 7)      → Stack size: 7
  Popped (76, 6)      → Stack size: 6
  Popped (72, 5)      → Stack size: 5

  Stack after top pops (bottom → top):
    [0] (73, 0) ← BOTTOM
    [1] (74, 1)
    [2] (75, 2)
    [3] (71, 3)
    [4] (69, 4) ← TOP

=======================================================
POPPING FROM THE MIDDLE (index 2)
=======================================================
  Popped (75, 2) from index [2]
  Stack size now: 4

  Stack after middle pop (bottom → top):
    [0] (73, 0) ← BOTTOM
    [1] (74, 1)
    [2] (71, 3)
    [3] (69, 4) ← TOP

=======================================================
POPPING ALL REMAINING ITEMS
=======================================================
  Popped (69, 4)      → Stack size: 3
  Popped (71, 3)      → Stack size: 2
  Popped (74, 1)      → Stack size: 1
  Popped (73, 0)      → Stack size: 0

  Stack is empty: []
=======================================================


"""
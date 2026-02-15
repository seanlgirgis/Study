
# Cheat Sheet #4: Advanced Structures & Graph-Like Problems

**Focus**: Matrix/grid killers (Q3), BFS/DFS traversal, heaps, and OOP simulations (Capital One favorite).  
**Target**: Solve hard grid problems in <20 min; implement class-based state machines cleanly.  
**Alignment**: Roadmap Phase C (Matrix Killer) + A.4 (Banking Simulations).  
**Mindset**: For grids → always use directions tuple + visited set. For simulations → track state with instance variables.

## 1. Matrices / 2D Arrays

**Traversal Patterns**
- Row-major: `for i in range(m): for j in range(n):`
- Column-major: `for j in range(n): for i in range(m):`

**Spiral Order (LC 54 – very common)**
```python
from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """Return elements in spiral order."""
    if not matrix or not matrix[0]:
        return []
    
    result = []
    m, n = len(matrix), len(matrix[0])
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        # Top row left → right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Right column top → bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Bottom row right → left (if still valid)
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        # Left column bottom → top (if still valid)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

## 1.5 Quick Direction Snippet
Copy-paste for any grid neighbor iteration (4-way).
```python
# Up, Down, Left, Right
for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        # traverse(nr, nc)
```
```

**Rotate Image 90° clockwise (LC 48)**
```python
def rotate(matrix: List[List[int]]) -> None:
    """Rotate matrix 90° clockwise in-place."""
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
```

**Edge Cases**
- 1×1 matrix
- Empty / None
- Non-square
- All same values

## 2. BFS / DFS on Grids

**BFS Template (deque – preferred for shortest path)**
```python
from collections import deque
from typing import List, Tuple

def bfs_grid(grid: List[List[int]], sr: int, sc: int) -> int:
    """BFS from (sr, sc) – example: return steps or -1 if unreachable."""
    if not grid or not grid[0]:
        return -1
    
    m, n = len(grid), len(grid[0])
    if not (0 <= sr < m and 0 <= sc < n):
        return -1
    
    visited: set[Tuple[int, int]] = {(sr, sc)}
    q = deque([(sr, sc, 0)])  # (row, col, steps)
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right left down up
    
    while q:
        r, c, steps = q.popleft()
        
        # Example goal check
        if grid[r][c] == 9:  # or some condition
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                # Add condition: if grid[nr][nc] != 0 (wall) or valid move
                visited.add((nr, nc))
                q.append((nr, nc, steps + 1))
    
    return -1
```

**DFS Template (recursive – good for counting islands)**
```python
def num_islands(grid: List[List[str]]) -> int:
    """Number of islands (1 = land, 0 = water)."""
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    
    def dfs(i: int, j: int) -> None:
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == "0":
            return
        visited[i][j] = True
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(i, j)
                count += 1
    return count
```

**Tip**: Prefer BFS for shortest path; DFS for counting / flooding. Use set for visited (faster than 2D list for sparse grids).

## 3. Heaps (Priority Queues)

```python
import heapq
from typing import List

# Min-heap (default)
heap: List[int] = [3, 1, 4]
heapq.heapify(heap)          # O(n)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)  # 1

# Max-heap trick
max_heap = [-x for x in [3, 1, 4]]
heapq.heapify(max_heap)
largest = -heapq.heappop(max_heap)  # 4

# Top K frequent (LC 347)
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    from collections import Counter
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

## 4. OOP Simulations (Capital One Loves These)

**Example: Simple Bank System (LC 2043 style)**
```python
from typing import List

class Bank:
    """Simple bank with accounts and transactions."""
    def __init__(self, balance: List[int]):
        self.balance = [0] + balance  # 1-indexed
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (1 <= account1 < len(self.balance) and 1 <= account2 < len(self.balance)):
            return False
        if self.balance[account1] < money:
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True
    
    def deposit(self, account: int, money: int) -> bool:
        if not (1 <= account < len(self.balance)):
            return False
        self.balance[account] += money
        return True
    
    def withdraw(self, account: int, money: int) -> bool:
        if not (1 <= account < len(self.balance)) or self.balance[account] < money:
            return False
        self.balance[account] -= money
        return True
```

**Tips**
- Validate indices / negative money
- Use list for balances (1-indexed common in problems)
- Return bool success/failure

**Other Classics**
- Design Parking System (LC 1603)
- Min Stack (LC 155)

## Edge Cases Checklist
- Empty grid / matrix
- 1×1 grid
- All walls / no path
- Invalid account / negative money
- Max grid size (m,n ≤ 100–400 typical)

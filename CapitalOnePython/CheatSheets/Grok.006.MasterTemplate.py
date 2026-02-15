from typing import List, Optional, Dict, Tuple
from collections import deque, defaultdict, Counter
import heapq
import bisect

# ==============================================================================
# 0. Quick Imports & Snippets
# ==============================================================================
"""
import math
INF = float('inf')
"""
# Directions: Up, Down, Left, Right
# for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

# ==============================================================================
# 1. Union Find (DSU) - Connected Components / Cycles
# ==============================================================================
class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

# ==============================================================================
# 2. Trie (Prefix Tree) - Word Search / Autocomplete
# ==============================================================================
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children: return False
            node = node.children[char]
        return node.is_end

# ==============================================================================
# 3. Bank Simulation (Capital One Style)
# ==============================================================================
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = [0] + balance  # 1-indexed conversion
        self.n = len(balance)

    def _is_valid(self, account: int) -> bool:
        return 1 <= account <= self.n

    def transfer(self, acc1: int, acc2: int, money: int) -> bool:
        if not (self._is_valid(acc1) and self._is_valid(acc2)): return False
        if self.balance[acc1] < money: return False
        self.balance[acc1] -= money
        self.balance[acc2] += money
        return True

    def deposit(self, acc: int, money: int) -> bool:
        if not self._is_valid(acc): return False
        self.balance[acc] += money
        return True

    def withdraw(self, acc: int, money: int) -> bool:
        if not self._is_valid(acc) or self.balance[acc] < money: return False
        self.balance[acc] -= money
        return True

# ==============================================================================
# 4. Standard Templates
# ==============================================================================

def binary_search_template(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

def bfs_template(grid: List[List[int]], start_r: int, start_c: int) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque([(start_r, start_c, 0)]) # r, c, dist
    visited = {(start_r, start_c)}
    
    while q:
        r, c, dist = q.popleft()
        # if r == target_r and c == target_c: return dist
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                # if grid[nr][nc] != obstacle:
                visited.add((nr, nc))
                q.append((nr, nc, dist + 1))
    return -1

def monotonic_stack(nums: List[int]) -> List[int]:
    """Next Greater Element"""
    stack = [] # indices
    res = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)
    return res

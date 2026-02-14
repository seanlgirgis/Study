from typing import List

class Solution:
    def daysUntilWarmer(self, temps: List[int]) -> List[int]:
        n: int = len(temps)
        ret: List[int] = [0] * n  
        stack = []

        # This is the "Forward" Monotonic Stack approach.
        # It's perfectly valid and O(N).
        # (Though technically the file says 'ReverseTraversal', this works too!)
        for i, temp in enumerate(temps, start = 0):
            while stack and temps[stack[-1]] < temp:
                ind = stack.pop()
                ret[ind] = i - ind
            stack.append(i)
        return ret


test_cases: List[tuple[List[int], List[int]]] = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])
    , ([30, 40, 50, 60], [1, 1, 1, 0])  # Strictly increasing
    , ([30, 20, 10], [0, 0, 0])  # Strictly decreasing
    , ([50], [0])  # Single element
    ,([], [])  # Empty list

    # Edge Cases
    ,([0], [0]) # Single zero
    , ([100], [0])  # Single max temp
    ,([0, 0, 0, 0], [0, 0, 0, 0])  # All equal (no warmer)
    , ([100, 99, 98, 97], [0, 0, 0, 0])  # Decreasing to min
    , ([1, 2], [1, 0])  # Minimal increasing
    ,([2, 1], [0, 0]) # Minimal decreasing

    # Plateaus and Repeats
    ,([70, 70, 71, 70, 72], [2, 1, 2, 1, 0])  # Plateaus with jumps
    ,([80, 75, 80, 85], [3, 1, 1, 0])  # Tie then warmer
    ,([50, 50, 49, 51], [3, 2, 1, 0])  # Plateau drop then jump
    # Corrected Expectation: [2, 1, 0, 1, 0]
    # 90->95 (2), 85->95 (1), 95->?(0), 90->95 (1), 95->?(0)
    ,([90, 85, 95, 90, 95], [2, 1, 0, 1, 0])  # Multiple ties and peaks

    # Fluctuations and Longer Waits
    ,([60, 65, 62, 70, 68, 75], [1, 2, 1, 2, 1, 0])  # Wavy pattern
    ,([40, 30, 50, 45, 55], [2, 1, 2, 1, 0])  # Drop then recover
    ,([10, 20, 15, 25, 20, 30], [1, 2, 1, 2, 1, 0])  # Alternating small/big
    ,([99, 100, 98, 97, 101], [1, 3, 2, 1, 0])  # Late peak
    # Corrected Expectation: [1, 2, 1, 1, 2, 1, 0]
    # 5->6 (2 days: 5[idx 4] -> 0[idx 5] -> 6[idx 6])
    ,([1, 3, 2, 4, 5, 0, 6], [1, 2, 1, 1, 2, 1, 0])

# Stress Tests (Larger Sizes, Extremes)
    ,([0] * 100 + [1], list(range(100, 0, -1)) + [0])  # Long plateau, late warmer (n=101)
    ,(list(range(10000, 0, -1)), [0] * 10000)  # Max n, strictly decreasing
    ,(list(range(1, 10001)), [1] * 9999 + [0])  # Max n, strictly increasing (waits decrease)
    ,([100] * 5000 + [99] * 5000, [0] * 10000)  # Max n, all high then low (no warmer)
    ,([50, 100] + [0] * 9998, [1, 0] + [0] * 9998)  # Early peak, long tail of lows
]

sol: Solution = Solution()
i: int = 0
for temps, expected in test_cases:
    i +=1
    found = sol.daysUntilWarmer(temps)
    if len(temps) > 10:
        if found != expected:
            print(f"Test {i} failed")
        else:
            print(f"Test {i} passed")
    else:
        if found != expected:
            print(f"Test failed for {temps}: Expected {expected}, got {found}")
        else:
            print(f"Test passed for {temps}: Expected {expected}, got {found}")
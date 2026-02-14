# Project: Capital-One-CodeSignal-Prep-2026
# Sprint: 150.Lead-Data-Engineer-CodeSignal-Sprint
# Phase: A.1.1 Traversal Patterns — Linear Scan with Index Tracking
# Date: February 13, 2026
# Problem: Consecutive Increasing Streak

from typing import List


class Solution:
    def longestIncreasingStreak(self, nums: List[int]) -> int:
        """
        Given an array of integers nums, return the length of the longest consecutive increasing streak in the array.
        A consecutive increasing streak is a sequence of adjacent elements where each element is strictly greater than the previous one.
        """
        cur: int 
        """ Edge Cases """
        if len(nums) == 0:
            return 0
 
        current_low: int = nums[0]
        streak_length: int = 1
        max_length: int = 1
        """ Main Logic """
        for i in range(1, len(nums)):
            if nums[i] > current_low :
                streak_length +=1
                current_low = nums[i]
            else:   
                max_length = max(max_length, streak_length)
                streak_length = 1
                current_low = nums[i]
        
        """ Clean streak logic """
        max_length = max(max_length, streak_length)
        return max_length



def main()->None:
    sol: Solution = Solution()
    test_cases: List[tuple[List[int], int]] = [
        ([1, 3, 5, 4, 7],          3),  # [1,3,5] → 3 elements
        ([2, 2, 2, 2, 2],          1),  # no increase anywhere → single element = 1
        ([1],                      1),  # single element = 1
        ([],                       0),  # empty = 0
        ([7, 8, 9, 11, 12, 13, 7], 6),  # [7,8,9,11,12,13] → 6 elements
        ([1, 2, 3, 4, 5],          5),  # whole array increases → 5 elements
        ([5, 4, 3, 2, 1],          1),  # strictly decreasing → single element = 1
        ([1, 3, 2, 4, 5, 1, 7, 8], 3),  # [2,4,5] → 3 elements (beats [7,8] = 2)
    ]

    for nums, expected in test_cases:
        found = sol.longestIncreasingStreak(nums)
        if found != expected:
            print(f"Test failed for {nums}: Expected {expected}, got {found}")
        else:
            print(f"Test passed for {nums}: Expected {expected}, got {found}")
    
    pass
    
    
if __name__ == "__main__":
    main()
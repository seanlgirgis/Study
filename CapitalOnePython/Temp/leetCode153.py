from typing import List
"""
    LC 153 Find Minimum in Rotated Sorted Array
    Test class declares binary search method search .
"""
class SeanSolution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array using O(log n) time.
        
        The idea is to use binary search and compare the middle element 'mid'
        with the 'right' element to determine which side is sorted and where the
        pivot (minimum element) lies.
        """
        left , right  = 0 , len(nums) - 1 
        
        # We use 'left < right' to stop when left == right, which will be the minimum.
        while left < right:
            mid = (left + right) // 2
            
            # If mid > right, it means the sequence from mid to right is NOT sorted (it's interrupted).
            # This implies the pivot (minimum) must be in the right half (excluding mid).
            # Example: [3, 4, 5, 1, 2], mid=5, right=2. 5 > 2. Min (1) is to the right.
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # If mid <= right, the sequence from mid to right IS sorted.
            # This implies the minimum is either at 'mid' or in the left half.
            # We keep 'mid' in the search space by setting right = mid.
            # Example: [5, 1, 2, 3, 4], mid=2, right=4. 2 <= 4. Min (1) is to the left.
            else:
                right = mid
                
        # When loop ends, left == right, pointing to the minimum element.
        return nums[left]
# Test Harness
def run_tests(solution_class):
    solver = solution_class()
    
    test_cases = [
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11,13,15,17], 11),
        ([1], 1),
        ([2,1], 1),
        ([3,1,2], 1)
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = solver.findMin(nums)
        
        if result == expected:
            print(f"Test Case {i+1}: Passed ✅")
        else:
            print(f"Test Case {i+1}: Failed ❌")
            print(f"   Input: {nums}")
            print(f"   Expected: {expected}")
            print(f"   Actual:   {result}")

run_tests(SeanSolution)
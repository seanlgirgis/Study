from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    """
    LeetCode 1004. Max Consecutive Ones III
    
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
    in the array if you can flip at most k 0's.
    """
    left = 0
    max_len = 0
    zeros_count = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_count += 1
            
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len

# ------------------------------------------------------------------
# Test Harness
# ------------------------------------------------------------------
def run_tests(func):
    test_cases = [
        # --- LeetCode examples ---
        ("Example 1", [1,1,1,0,0,0,1,1,1,1,0], 2, 6),
        ("Example 2", [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
        
        # --- Edge cases ---
        ("All ones, k=0", [1,1,1,1], 0, 4),
        ("All zeros, k=2", [0,0,0,0], 2, 2),
        ("k >= len(nums)", [0,1,0,1], 5, 4),
        ("Empty nums", [], 0, 0),
        ("Alternating, k=1", [1,0,1,0,1], 1, 3),
    ]

    print(f"Running tests for: {func.__name__}\n")
    passed = 0
    for desc, nums, k, expected in test_cases:
        result = func(nums, k)
        if result == expected:
            print(f"✅ {desc}: Passed")
            passed += 1
        else:
            print(f"❌ {desc}: Failed")
            print(f"   Input: nums={nums}, k={k}")
            print(f"   Expected: {expected}")
            print(f"   Actual:   {result}")
        print("-" * 30)
    print(f"\n{passed}/{len(test_cases)} passed\n")

run_tests(longestOnes)

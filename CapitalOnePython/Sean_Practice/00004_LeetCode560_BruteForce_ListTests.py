from typing import List, Tuple

class SolutionBruteForce:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Calculates the number of subarrays that sum to k using a O(N^2) Brute Force approach.
        """
        count = 0
        n = len(nums)
        
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                
                if current_sum == k:
                    count += 1
                    
        return count

def run_tests_with_list_approach():
    print("--- LeetCode 560: Subarray Sum Equals K (Brute Force Test Harness) ---\n")
    
    sol = SolutionBruteForce()
    
    # ---------------------------------------------------------
    # Test Cases List: (description, input_nums, input_k, expected_output)
    # ---------------------------------------------------------
    test_cases = [
        # 1. Basic Positive Numbers
        ("Basic Case 1", [1, 1, 1], 2, 2),
        ("Basic Case 2", [1, 2, 3], 3, 2), # [1, 2], [3]
        
        # 2. Zeroes Handling
        ("Zeroes Case 1", [0, 0, 0], 0, 6), # [0], [0,0], [0,0,0], [0], [0,0], [0]
        ("Zeroes Case 2", [1, 0, 1], 2, 1), 

        # 3. Negative Numbers
        ("Negatives Case 1", [1, -1, 0], 0, 3), 
            # [1, -1] -> 0
            # [1, -1, 0] -> 0
            # [-1] -> -1
            # [-1, 0] -> -1
            # [0] -> 0
            # Total 3. Correct.
        
        ("Negatives Case 2", [-1, -1, 1], 0, 1), # [-1, 1] -> 0.

        # 4. Mixed / Complex
        ("Mixed Positive/Negative", [3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
            # [3, 4] = 7
            # [7] = 7
            # [7, 2, -3, 1] -> 7+2-3+1 = 7
            # [1, 4, 2] = 7
            # Total 4.

        # 5. Edge Cases
        ("Empty List", [], 0, 0),
        ("Single Element Match", [5], 5, 1),
        ("Single Element No Match", [5], 3, 0),
        
        # 6. No Solution
        ("No Solution", [1, 2, 3], 10, 0),
    ]

    # ---------------------------------------------------------
    # Execution Loop
    # ---------------------------------------------------------
    all_passed = True
    
    for idx, (desc, nums, k, expected) in enumerate(test_cases):
        print(f"Test {idx + 1}: {desc}")
        print(f"  Input: nums={nums}, k={k}")
        
        # Run the solution
        actual = sol.subarraySum(nums, k)
        
        if actual == expected:
            print(f"  Result: {actual} (PASS) ✅")
        else:
            print(f"  Result: {actual} (FAIL) ❌")
            print(f"  Expected: {expected}")
            all_passed = False
            
        print("-" * 40)
        
    if all_passed:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print("\n⚠️ SOME TESTS FAILED. CHECK OUTPUT ABOVE.")

if __name__ == "__main__":
    run_tests_with_list_approach()

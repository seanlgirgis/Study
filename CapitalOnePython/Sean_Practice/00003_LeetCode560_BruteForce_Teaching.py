import time
from typing import List

class SolutionBruteForce:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Calculates the number of subarrays that sum to k using a Brute Force approach.
        
        Time Complexity: O(N^2) - We have two nested loops.
        Space Complexity: O(1)   - We only store a few variables.
        """
        count = 0
        n = len(nums)
        
        # Outer loop: picks the starting point of the subarray
        for start in range(n):
            current_sum = 0
            
            # Inner loop: extends the subarray from 'start' to 'end'
            # This intuitively represents checking every possible contiguous slice.
            for end in range(start, n):
                current_sum += nums[end]
                
                # Check if the current subarray sum equals k
                if current_sum == k:
                    count += 1
                    
        return count

def run_performance_demo():
    print("--- LeetCode 560: Subarray Sum Equals K (Brute Force) ---\n")
    
    sol = SolutionBruteForce()
    
    # 1. Correctness Test
    print("1. Running Small Correctness Test...")
    nums_small = [1, 1, 1]
    k_small = 2
    result_small = sol.subarraySum(nums_small, k_small)
    print(f"Input: nums={nums_small}, k={k_small}")
    print(f"Output: {result_small}")
    print(f"Expected: 2")
    assert result_small == 2
    print("✅ Passed 'Standard Case'!\n")

    # 1.1 Edge Case: Negative Numbers
    print("1.1 Testing Negative Numbers...")
    # Subarrays summing to 0: [1, -1], [-1, 1] -> Count: 2
    # Oh wait, k=0. 
    # [1, -1] = 0
    # [-1, 1] = 0
    # [1, -1, 1] ... no
    nums_neg = [1, -1, 1]
    k_neg = 0
    # subarrays: [1] (1), [1, -1] (0)*, [1, -1, 1] (1), [-1] (-1), [-1, 1] (0)*, [1] (1)
    result_neg = sol.subarraySum(nums_neg, k_neg)
    print(f"Input: nums={nums_neg}, k={k_neg}")
    print(f"Output: {result_neg} | Expected: 2")
    assert result_neg == 2
    print("✅ Passed 'Negative Numbers'!\n")

    # 1.2 Edge Case: Zeroes
    print("1.2 Testing Zeroes...")
    nums_zero = [0, 0, 0]
    k_zero = 0
    # subarrays:
    # [0] (idx 0)
    # [0, 0] (idx 0-1)
    # [0, 0, 0] (idx 0-2)
    # [0] (idx 1)
    # [0, 0] (idx 1-2)
    # [0] (idx 2)
    # Total: 6
    result_zero = sol.subarraySum(nums_zero, k_zero)
    print(f"Input: nums={nums_zero}, k={k_zero}")
    print(f"Output: {result_zero} | Expected: 6")
    assert result_zero == 6
    print("✅ Passed 'All Zeroes'!\n")


    # 2. Performance Test
    print("2. Running Large Performance Test (O(N^2) Demonstration)...")
    N = 10000  # 10,000 elements
    print(f"Generating input array of size N = {N}...")
    
    # Create an array where no subarray sums to k (worst case ensures we check everything)
    nums_large = [1] * N
    k_large = N * 2  # Impossible sum, so count remains 0, but loops run fully.
    
    print("Starting Brute Force calculation...")
    start_time = time.time()
    
    count_large = sol.subarraySum(nums_large, k_large)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Calculation finished in {elapsed_time:.4f} seconds.")
    print(f"Result: {count_large}")
    
    print("\n--- Why is this slow? ---")
    print(f"Input size N = {N}")
    print(f"The outer loop runs {N} times.")
    print(f"The inner loop runs roughly {N}/2 times on average.")
    print(f"Total operations approx: ({N} * {N}) / 2 = {(N*N)//2} iterations.")
    print("For N=20,000, this would take 4x longer (quadratic growth).")
    print("This is why O(N^2) usually leads to Time Limit Exceeded (TLE) on LeetCode for N > 10^4.")

if __name__ == "__main__":
    run_performance_demo()

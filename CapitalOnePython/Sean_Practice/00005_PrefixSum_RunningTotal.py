from typing import List
import numpy as np
def get_running_total(nums: List[int], k:int) -> List[int]:
    """
    Returns a new array where each element is the running total 
    of the input array up to that index, starting with 0.
    Length will be len(nums) + 1.
    """
    if not nums:
        return [0]
    
    # Initialize with 0 as requested
    running_totals = [0]
    current_sum = 0
    
    for num in nums:
        current_sum += num
        running_totals.append(current_sum)
        
    return running_totals

if __name__ == "__main__":
    input_array = [3, 4, 7, 2, -3, 1, 4, 2]
    result = get_running_total(input_array)
    
    print(f"Input Array:   {input_array}")
    print(f"Running Total: {result}")

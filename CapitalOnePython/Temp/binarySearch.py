from typing import List

def binary_search(arr: List[int], target: int) -> bool:
    """
    Returns True if target is found, False otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Integer division
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return False  # Not found


# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(binary_search(sorted_list, 7))   # Output: True
print(binary_search(sorted_list, 4))   # Output: False
print(binary_search(sorted_list, 19))  # Output: True
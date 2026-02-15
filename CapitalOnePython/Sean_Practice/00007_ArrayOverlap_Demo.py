from typing import List
from collections import Counter

def count_occurrences_demo():
    # Array 1: Original Prefix Sums
    arr1 = [0, 3, 7, 14, 16, 13, 14, 18, 20]
    
    # Array 2: (Prefix Sums - k) effectively
    arr2 = [-7, -4, 0, 7, 9, 6, 7, 11, 13]
    
    print(f"Array 1 (Target): {arr1}")
    print(f"Array 2 (Seekers):{arr2}\n")

    # ---------------------------------------------------------
    # Efficient Approach: Hash Map (Frequency Map)
    # Time Complexity: O(N + M) 
    # ---------------------------------------------------------
    
    # 1. Create a frequency map of elements in Array 1
    # This tells us: "How many times does value X appear in Array 1?"
    counts_arr1 = Counter(arr1)
    
    total_matches = 0
    
    print("--- Step-by-Step Check ---")
    for val in arr2:
        if val in counts_arr1:
            count = counts_arr1[val]
            print(f"Value {val} found in Array 1 -> {count} times")
            total_matches += count
        else:
            # print(f"Value {val} NOT found in Array 1") # Optional for noise reduction
            pass
            
    print("-" * 30)
    print(f"Total Occurrences Found: {total_matches}")

if __name__ == "__main__":
    count_occurrences_demo()

from typing import List

def demonstrate_subtraction():
    running_totals = [0, 3, 7, 14, 16, 13, 14, 18, 20]
    k = 7
    
    print(f"Original Array: {running_totals}")
    print(f"Value to subtract (k): {k}\n")

    # Method 1: List Comprehension (Most Pythonic & Easiest Syntax)
    # Syntax: [x - k for x in list]
    result_list_comp = [x - k for x in running_totals]
    print(f"Method 1 (List Comprehension): {result_list_comp}")
    print("Syntax: [x - k for x in running_totals]  <-- RECOMMENDED\n")

    # Method 2: Map with Lambda (Functional style)
    # Syntax: list(map(lambda x: x - k, list))
    result_map = list(map(lambda x: x - k, running_totals))
    print(f"Method 2 (Map & Lambda):       {result_map}")
    print("Syntax: list(map(lambda x: x - k, running_totals))\n")

    # Method 3: NumPy (If you are doing data science/heavy math)
    # Syntax: arr - k
    try:
        import numpy as np
        arr_np = np.array(running_totals)
        result_np = arr_np - k
        print(f"Method 3 (NumPy):              {result_np}")
        print("Syntax: numpy_array - k  <-- Easiest if using NumPy\n")
    except ImportError:
        print("Method 3 (NumPy):              NumPy not installed (skipped)")

if __name__ == "__main__":
    demonstrate_subtraction()

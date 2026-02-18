
import random
from typing import List, Tuple

def create_sorted_matrix(m: int, n: int, exists: bool = True) -> Tuple[List[List[int]], int]:
    """
    Creates an m x n matrix where:
    - Each row is sorted from left to right.
    - The first integer of each row is greater than the last integer of the previous row.
    - All elements are unique and random.
    
    Args:
        m: Number of rows
        n: Number of columns
        exists: If True, returns a target present in the matrix. If False, returns a target NOT present.

    Returns:
        matrix: The generated m x n matrix.
        target: A random unique number that exists (or not) within the matrix based on 'exists'.
    """
    if m <= 0 or n <= 0:
        return [], -1

    total_elements = m * n
    
    # Start with a random base number
    current_val = random.randint(1, 100)
    
    # Generate sorted unique numbers
    # We add a random increment (1 to 10) to ensure uniqueness and sorted order
    flat_list = []
    gaps = []
    for i in range(total_elements):
        increment = random.randint(1, 10)
        prev_val = current_val
        current_val += increment
        flat_list.append(current_val)
        
        # Check for gap between previous and current (if increment > 1)
        # Note: current_val - prev_val = increment. Gap exists if increment > 1.
        if increment > 1:
            # All numbers in (prev_val, current_val) are candidates
            for gap_val in range(prev_val + 1, current_val):
                gaps.append(gap_val)

    # Reshape into m x n matrix
    matrix = []
    for i in range(m):
        row = flat_list[i*n : (i+1)*n]
        matrix.append(row)
        
    if exists:
        target = random.choice(flat_list)
    else:
        # Pick a random missing number
        if gaps:
            target = random.choice(gaps)
        else:
            # Fallback: pick a number outside the range
            target = flat_list[-1] + 1
            
    return matrix, target


"""
LEC 74.
Since the matrix is unique sorted in each row. 
a simple trick to do the search is to think of it as a long list
of numbers sorted.

just by creaating a Matrix2D2List class. ... Loading the dimensions.
we can get things like. index of first item. index of last item. length
we can also get mid point...
We can get the item at these positions and their values.
We can translate a list position to a matrix position.
Doing that, we can treat the search as any normal binary search
to make lige easy.. Our class  will handle the pointers on the list . This will make the code easy to implement.
the class will keep track of right and left pointers and can mode one of them 
to a  a middle position; it can even shift a pointer left or right


"""
class Matrix2D2List:
    def __int__(self, _r: int, _c: int , _matrix: List[List[int]] ):
        self.r = _r
        self.c = _c 
        self.matrix = _matrix
        self.length = _r * _c    # Items in the list are are numberd 0 to self.length -1 
        self.left = 0
        self.right = self.length - 1















if __name__ == "__main__":
    m, n = 3, 4
    
    # Test Existing
    matrix, target = create_sorted_matrix(m, n, exists=True)
    print(f"Generated {m}x{n} Matrix (Target Exists):")
    for row in matrix:
        print(row)
    print(f"Random Target (Exists): {target}")
    
    print("-" * 20)
    
    # Test Non-Existing
    matrix, target = create_sorted_matrix(m, n, exists=False)
    print(f"Generated {m}x{n} Matrix (Target Not Exists):")
    for row in matrix:
        print(row)
    print(f"Random Target (Not Exists): {target}")

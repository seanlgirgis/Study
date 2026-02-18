
import random
from typing import List, Tuple
import sys

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
    def __init__(self, r: int, c: int , matrix: List[List[int]] ):
        self._r = r
        self._c = c
        self._matrix = matrix
        self._length = r * c    # Items in the list are are numberd 0 to self.length -1 
        self._left = 0
        self._right = self._length - 1
        self._mid = (self._left + self._right) //2

    def index_to_position(self, index: int) -> tuple[int, int]:
        """Given a linear index (0 to m*n-1), return the (row, col) tuple in the matrix."""
        if index < 0 or index >= self._length:
            raise IndexError(f"Index {index} out of range for {self._length}-element matrix")
        row = index // self._cols
        col = index % self._cols
        return (row, col)


    def position_to_index(self, row: int, col: int) -> int:
        """Given a (row, col) matrix position, return the linear index."""
        if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
            raise IndexError(f"Position ({row}, {col}) out of bounds for {self._rows}x{self._cols} matrix")
        return row * self._cols + col


    def value_at_position(self, row: int, col: int):
        """Given a (row, col) tuple, return the matrix value at that position."""
        if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
            raise IndexError(f"Position ({row}, {col}) out of bounds")
        return self._matrix[row][col]


    def value_at_index(self, index: int):
        """Given a linear index, return the matrix value at that position."""
        row, col = self.index_to_position(index)
        return self._matrix[row][col]


    def mid(self)->None:
        # recalculates the mid position
        self._mid = (self._left + self._right) //2

    def pprint(self) -> None:
        """Pretty print the matrix in grid form with aligned columns."""
        # Find the widest value for consistent column alignment
        max_width = max(len(str(self._matrix[r][c])) 
                        for r in range(self._rows) 
                        for c in range(self._cols))
        
        col_separator = " | "
        row_separator = "-" * (max_width * self._cols + len(col_separator) * (self._cols - 1) + 4)
        
        print(row_separator)
        for r in range(self._rows):
            row_str = col_separator.join(str(self._matrix[r][c]).rjust(max_width) for c in range(self._cols))
            print(f"| {row_str} |")
        print(row_separator)


    def plprint(self) -> None:
        """Pretty print the flat list representation with index labels."""
        max_width = max(len(str(self._matrix[r][c])) 
                        for r in range(self._rows) 
                        for c in range(self._cols))
        
        max_idx_width = len(str(self._length - 1))
        
        # Print index headers
        index_header = "  ".join(f"[{str(i).rjust(max_idx_width)}]" for i in range(self._length))
        print(index_header)
        
        # Print values aligned under their index
        cell_width = max_idx_width + 2  # accounts for the brackets [ ]
        values = "  ".join(str(self.value_at_index(i)).rjust(cell_width) for i in range(self._length))
        print(values)
        
        # Print (row,col) tuple labels under each value
        tuple_labels = "  ".join(f"{str(self.index_to_position(i)).rjust(cell_width)}" for i in range(self._length))
        print(tuple_labels)





"""
    main method to search for an item in a sorted matrix and return
    True if item is found.  return false if item is not found.
    The method will implement a binary search



"""

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    return False






if __name__ == "__main__":
    m, n = 3, 4
    
    # Test Existing
    mat, target = create_sorted_matrix(m, n, exists=True)
    print(f"Generated {m}x{n} Matrix (Target Exists):")
    for row in mat:
        print(row)
    print(f"Random Target (Exists): {target}")

    #using matrix and m and n we will test and simpulate the usage of 
    # the class Matrix2D2List
    matrix: Matrix2D2List = Matrix2D2List(m,n, mat)

    print (matrix._length)







    sys.exit(0)
    print("-" * 20)
    
    # Test Non-Existing
    matrix, target = create_sorted_matrix(m, n, exists=False)
    print(f"Generated {m}x{n} Matrix (Target Not Exists):")
    for row in matrix:
        print(row)
    print(f"Random Target (Not Exists): {target}")

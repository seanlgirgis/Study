"""
    Leet 54
    Display contents of a matrix in a spiral method right, down, left, up, right, ... 
    New implementation .. Clever. No repeating lines of code

"""

from typing import List, Tuple
import random

class Matrix_helper:
    """
        Example Usage: -
            helper = Matrix_helper()
            matrix = helper.create_random_matrix(5,9)
            Matrix_helper.pprint(matrix)
            coords = [(0,4), (0,3), (0,2), (0,1)]
            print(f"Series for {coords}: {Matrix_helper.get_series(matrix, coords)}")

            print("-" * 20)
            Matrix_helper.zero_series(matrix, coords)
            Matrix_helper.pprint(matrix)
    
    """
    def create_random_matrix(self, m: int, n: int) -> List[List[int]]:
        """
        Creates an m×n matrix filled with random two-digit integers (10 to 99).

        Args:
            m: Number of rows
            n: Number of columns

        Returns:
            2D list (matrix) with random values in [10, 99]

        
        """
        # Using list comprehension for clarity and efficiency
        random.seed(42)
        self.m = m
        self.n = n
        return [[random.randint(10, 99) for _ in range(n)] for _ in range(m)]
    
    @staticmethod
    def zero_series(matrix: List[List[int]], coords: List[Tuple[int, int]]) -> None:
        for r, c in coords:
            matrix[r][c] = 0

    @staticmethod
    def pprint(matrix: List[List[int]])->None:
        for row in matrix:
            # Use 02d format to print 0 as 00
            print(" ".join(f"{x:02d}" if x == 0 else f"{x:2d}" for x in row))

    @staticmethod
    def get_series(matrix: List[List[int]], coords: List[Tuple[int, int]]) -> List[int]:
        # User implies (x=col, y=row) coordinates
        return [matrix[r][c] for r, c in coords]
    


def direction_pattern():
    while True:
        yield 1
        yield 1
        yield -1
        yield -1 

def traverse_type():
    while True:
        yield 1
        yield -1  


def generate_segment(
    length: int,
    entry: Tuple[int, int],
    type: int,           # 1 = horizontal (row), -1 = vertical (column)
    direction: int = 1   # 1 = increasing index, -1 = decreasing index
) -> List[Tuple[int, int]]:
    """
    Generates a straight segment of 'length' cells.
    Starts from the cell immediately after the given 'entry' cell,
    moves either horizontally (type=1) or vertically (type=-1),
    in the direction of increasing (+1) or decreasing (-1) indices.
    
    No boundary checks, no input validation — assumes correct usage.
    
    Examples of your usage pattern:
        generate_segment(10, (-1, 0), type=1, direction=1)
        → starts at (0,0) → goes right → [(0,0), (0,1), ..., (0,9)]

        generate_segment(6, (5, -1), type=1, direction=-1)
        → starts at (5,0) → goes left → [(5,0), (5,-1), (5,-2), ..., (5,-5)]

        generate_segment(8, (-1, 7), type=-1, direction=1)
        → starts at (0,7) → goes down → [(0,7), (1,7), ..., (7,7)]
    """
    r, c = entry

    if type == 1:           # horizontal — change column
        start_r = r
        start_c = c + direction  # step into the row from entry
        dr, dc = 0, direction
    else:                   # vertical — change row
        start_r = r + direction
        start_c = c
        dr, dc = direction, 0

    path: List[Tuple[int, int]] = []
    cr, cc = start_r, start_c

    for _ in range(length):
        path.append((cr, cc))
        cr += dr
        cc += dc

    return path



class Solution:

    def length_toTravel(self, row_col:int)->int:
        if row_col == 1:
            self.row_length -= 1
            return self.row_length
        else:
            self.col_length -= 1
            return self.col_length
    
    def SpiralOrder(self, matrix: List[List[int]])->List[int]:
        if not matrix or not matrix[0]:   # ← this line protects everything
            return []
        
        Matrix_helper.pprint(matrix)
        ret:List[int]= []
        m = len(matrix)   #number of rows
        n = len(matrix[0]) #number of columns

        self.row_length: int = n + 1
        self.col_length: int = m
        
        direction = direction_pattern()
        row_col = traverse_type()
        
        cell_at : Tuple[int,int] = (0,-1)
        
        while True:
            xy = next(row_col)
            point_to = next(direction)
            l:int = self.length_toTravel(xy)
            
            if l <= 0:
                break
                
            print(f" Row Or Col {xy}  point_to {point_to}   cell_at {cell_at}    with length {l} ")
            seg = generate_segment(l, cell_at, xy, point_to)
            #print(seg)
            
            ret.extend(Matrix_helper.get_series(matrix, seg))
            Matrix_helper.zero_series(matrix, seg)
            Matrix_helper.pprint(matrix)
            
            cell_at = seg[-1]

        return ret

sol = Solution()
n,m = 4,5
print(sol.SpiralOrder(Matrix_helper().create_random_matrix(n,m)))

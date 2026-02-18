import sys
from enum import Enum
from typing import List, Tuple


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




def direction_pattern():
    while True:
        yield 1
        yield 1
        yield -1
        yield -1
pattern = direction_pattern()

matrix = [[(r * 4 + c + 1) for c in range(4)] for r in range(5)]
for row in matrix:
    print(row)


m, n = len(matrix), len(matrix[0])
print(m, n)

row_length: int = 4 + 1
col_length: int = 5
step: int = 0

def length_toTravel(ax:int)->int:
    global row_length, col_length
    if ax == 1:
        row_length -= 1
        return row_length
    else:
        col_length -= 1
        return col_length

Axis = Enum('Axis', {'ROW': 1, 'COL': -1})
dr = Enum('dr', {'Increasing': 1, 'Decreasing': -1})

ax:int = -1

cnt:int  = 0

cnt+=1
ax *= -1
l:int = length_toTravel(ax)

print(generate_segment(15, (0,-1), 1, 1))
print(generate_segment(15, (0,-1), 1, 1)[-1])
first_cell : Tuple[int,int] = (0,-1)

while l > 0:
    print (cnt , '-' * 25)
    pat = next(pattern)
    seg = generate_segment(l, first_cell, ax, pat)
    print(seg)
    first_cell = seg[-1] if seg else (-1, -1)
    #print (f" {Axis(ax).name}   {dr(next(pattern)).name}   length is {l}")
    #print(ax , pat)

    cnt+=1
    ax *= -1
    l = length_toTravel(ax)


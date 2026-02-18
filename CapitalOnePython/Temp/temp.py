from typing import List


class Grid:
    def __init__(self, _g: List[List[str]]):
        self.g = _g
        self.rows = len(self.g)
        self.cols = len(self.g[0]) if self.g else 0
        self.num_islands = 0
        self.islands = []

    def nextIslandStr(self) -> str:
        self.num_islands += 1
        s = str(self.num_islands + 10)
        self.islands.append(s)
        return s

    def draw(self):
        # Header with column indices
        print("   " + " ".join(f"{i:2}" for i in range(self.cols)))
        print("  +" + "--" * self.cols + "-+")

        for i, row in enumerate(self.g):
            line = f"{i:2}|"
            for cell in row:
                line += f" {cell:1} "
            line += "|"
            print(line)
            # print("  +" + "--" * self.cols + "-+")
        # s = self.nextIslandStr()
        # print(self.islands)


    def markIslandAround(self, r: int, c: int) -> None:
        cur_marker = self.g[r][c]
        # If it is not 1.. it is already marked island
        # If you are here you are in land.. check if new island or continuation
        if cur_marker == "1":
            island_marker = self.checkAdjIsland(r, c)
            if island_marker == "":
                island_marker = self.nextIslandStr()
            self.g[r][c] = island_marker
            cur_marker = island_marker
        
        # Propagate if needed (though simplistic here, markUpTo4Cells handles recursion)
        self.markUpTo4Cells(r, c, cur_marker)

    def markUpTo4Cells(self, r: int, c: int, marker: str) -> None:
        # Check 4 directions
        # Up
        self.markIt(r - 1, c, marker)
        # Down
        self.markIt(r + 1, c, marker)
        # Left
        self.markIt(r, c - 1, marker)
        # Right
        self.markIt(r, c + 1, marker)

    def markIt(self, r: int, c: int, marker: str) -> None:
        if r >= 0 and r < self.rows and c >= 0 and c < self.cols:
            if self.g[r][c] == "1":
                self.g[r][c] = marker
                self.markUpTo4Cells(r, c, marker)

    def cell_label(self, r: int, c: int) -> str:  # return "" for out of range.. if in range, return label
        if r < 0 or r >= self.rows: return ""
        if c < 0 or c >= self.cols: return ""
        return self.g[r][c]

    def checkAdjIsland(self, r: int, c: int) -> str:
        # Check 4 directions
        # Up
        cell_above = self.cell_label(r - 1, c)
        if cell_above not in ("0", "1", ""): return cell_above
        # Down
        cell_below = self.cell_label(r + 1, c)
        if cell_below not in ("0", "1", ""): return cell_below
        # Left
        cell_left = self.cell_label(r, c - 1)
        if cell_left not in ("0", "1", ""): return cell_left
        # Right
        cell_right = self.cell_label(r, c + 1)
        if cell_right not in ("0", "1", ""): return cell_right

        return ""

    def numIslands(self) -> int:
        for r in range(self.rows):
            for c in range(self.cols):
                if self.g[r][c] == "1":
                    self.markIslandAround(r, c)

        return self.num_islands


def numIslands(grid: List[List[str]]) -> int:

    """
    LeetCode 200. Number of Islands
    
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
    return the number of islands.
    Solution:-
        Traverse .. if "1" mark as "X" .. Increment island start an island search in all adjacent.. Until island complete
         Once an island is done... search more.. if zero od X is water or island counted.
    """
    g_obj = Grid(grid)
    return g_obj.numIslands()



# ------------------------------------------------------------------
# Test Harness
# ------------------------------------------------------------------
def run_tests():
    test_cases = [
        # --- LeetCode examples ---
        ("Example 1", [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ], 1),
        ("Example 2", [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ], 3),

        # --- Edge cases ---
        ("Empty grid", [], 0),
        ("All water", [["0","0"],["0","0"]], 0),
        ("All land", [["1","1"],["1","1"]], 1),
        ("Single cell land", [["1"]], 1),
        ("Single cell water", [["0"]], 0),
        ("Diagonal (disconnected)", [
            ["1","0","1"],
            ["0","1","0"],
            ["1","0","1"]
        ], 5),
    ]

    print(f"Running tests for: numIslands\n")
    passed = 0
    import copy
    
    for desc, grid, expected in test_cases:
        # Deep copy to allow in-place modification (visited marking) without affecting next test run if passed by ref
        grid_copy = copy.deepcopy(grid)
        
        # Capture stdout to avoid cluttering test output with island drawings, 
        # unless you want to see them. For now, let's just print the result.
        # But wait, user asked "maybe also draw the final map".
        
        print(f"--- Test: {desc} ---")
        g_obj = Grid(grid_copy)
        result = g_obj.numIslands()
        
        if result == expected:
            print(f"✅ Passed")
            passed += 1
        else:
            print(f"❌ Failed")
            print(f"   Input: {grid}")
            print(f"   Expected: {expected}")
            print(f"   Actual:   {result}")
            
        # Draw the final map as requested
        if g_obj.rows > 0 and g_obj.cols > 0:
             print("Final Map:")
             g_obj.draw()
        print("-" * 30)
        
    print(f"\n{passed}/{len(test_cases)} passed\n")

if __name__ == "__main__":
    run_tests()

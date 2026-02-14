from typing import List

class Solution:
    def daysUntilWarmer(self, temps: List[int]) -> List[int]:
        n: int = len(temps)
        ret: List[int] = [0] * n  
        stack: List[int] = []
        print(f"Temps is {temps}")
        for x, temp in enumerate(reversed(temps)):
            
            i = n - 1 - x  # ← Calculate i FIRST, outside any while loop
            print ("*"* 50)
            print(f"Iteration {x} Temp is {temp} Index is {i}")
            if stack:
                print(f"Top of the stack is {stack[-1]} and temp is {temps[stack[-1]]}")
            # Single while loop to pop non-warmer elements
            while stack and temps[stack[-1]] <= temp:
                stack.pop()
            
            # Check result AFTER popping if any left in the stack.. we found the first warmer day
            if stack:
                print(f"Found warmer day at index {stack[-1]} and temp is {temps[stack[-1]]} While current index is {i} and temp is {temp} so the offset is {stack[-1] - i} ")
                ret[i] = stack[-1] - i  # ← calc distance between current index and the first warmer day
            
            # ALWAYS push current index
            stack.append(i)
            self.printStackValues(stack, temps)
            print(f"Ret is {ret}")
            print("\n")
        return ret  # ← Outside the for loop

    def printStackValues(self, stack: List[int], temps: List[int]) -> None:
        # Map indices in stack back to their temperature values
        values = [temps[i] for i in stack]
        print(f"Stack Indices: {stack}")
        print(f"Stack Values:  {values}")

        
    def runSuite(self, test_cases: List[tuple[List[int], List[int]]]):
        for i, (temps, expected) in enumerate(test_cases):
            found = self.daysUntilWarmer(temps)
            if len(temps) > 10:
                if found != expected:
                    print(f"Test {i} failed")
                else:
                    print(f"Test {i} passed")
            else:
                if found != expected:
                    print(f"Test failed for {temps}: Expected {expected}, got {found}")
                else:
                    print(f"Test passed for {temps}: Expected {expected}, got {found}")
    
sol: Solution = Solution()

test_cases: List[tuple[List[int], List[int]]] = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])

]
sol.runSuite(test_cases)        
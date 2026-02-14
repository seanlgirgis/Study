from typing import List

class Solution:

    def findLengthOfLCIS(self,nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        ret = 0
        current_length = 0
        max_length = 0
        for i, num in enumerate(nums):
            if i == 0:
                current_length = 1
                max_length = 1
            else:
                if num > nums[i-1]:
                    current_length += 1
                else:
                    current_length = 1
                max_length = max(max_length, current_length)
        return max_length


    def runSuite(self, test_cases: List[tuple[List[int], int]]):
        for i, (lst, expected) in enumerate(test_cases):
            found = self.findLengthOfLCIS(lst)
            if len(lst) > 10:
                if found != expected:
                    print(f"Test {i} failed")
                else:
                    print(f"Test {i} passed")
            else:   
                if found != expected:
                    print(f"Test failed for {lst}: Expected {expected}, got {found}")
                else:
                    print(f"Test passed for {lst}: Expected {expected}, got {found}")

test_cases: List[tuple[List[int], int]] = [
    ([1, 3, 5, 4, 7], 3)
    ,([],0)
    ,([2, 2, 2, 2, 2],1)
    ,([1, 2, 3, 0, 1, 2, 3, 4],5)
     ,([8],1)
]

sol: Solution = Solution()
sol.runSuite(test_cases)
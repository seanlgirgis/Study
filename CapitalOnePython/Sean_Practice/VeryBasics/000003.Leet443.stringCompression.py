from typing import List

class Solution:
    def compress(self, chars: List[str]) -> (int, List[str]):
        n = len(chars)
        ret = []
        if n == 0:
            return (0, [])
       
        current_streak = 0
        for i, char in enumerate(chars):
            if i == n-1 or (char != chars[i+1]):
                current_streak += 1
            else:
                ret.append(char)
                if current_streak > 1:
                    ret.append(str(current_streak))
                current_streak = 0
                

            

        # Your code here
        
        return (len(ret), ret)

    def runSuite(self, test_cases: List[tuple[List[str], int, List[str]]]):
        for i, (chars_input, expected_len, expected_chars) in enumerate(test_cases):
            # Make a copy since we modify in-place
            result_len, result_chars = self.compress(chars_input)
            
            if result_len != expected_len or result_chars != expected_chars:
                print(f"Test {i} FAILED")
                print(f"  Input:    {chars_input}")
                print(f"  Expected: {expected_chars} (len={expected_len})")
                print(f"  Got:      {result_chars} (len={result_len})")
            else:
                print(f"Test {i} PASSED: {chars_input} → {result_chars}")

test_cases: List[tuple[List[str], int, List[str]]] = [
    (["a","a","b","b","c","c","c"], 6, ["a","2","b","2","c","3"])
]

sol = Solution()
sol.runSuite(test_cases)
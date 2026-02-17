from collections import Counter
import sys

class Window:
    def __init__(self, s: str, t: str):
        self.s = s
        self.t = t
        self.sLength = len(s)
        self.left = 0
        self.right = 0
        self.length = 1
        self.need = Counter(t)
        self.have = self._getEmptyHave()
        self._updateHaveAdd(s[0])

    def _getEmptyHave(self)->Counter: #Inner helper method
        return  Counter({key: 0 for key in self.need})

    def _updateLength(self): #Inner helper method
        self.length = self.right - self.left + 1
    
    def _updateHaveAdd(self, ch: str)->None: #Inner helper method
        if ch in self.have:
            self.have[ch] += 1

    def _updateHaveRemove(self, ch: str)->None: #Inner helper method
        if ch in self.have:
            self.have[ch] -= 1

    def matches(self)->bool:
        """
         Calculates matches for have has at least the same combination as need
        """
        for ch in self.need:
            if self.have[ch] < self.need[ch]:
                return False
        return True

    def wind(self)->str:
        return self.s[self.left:self.right+1]

    def expand(self)->bool:
        """
            expanding; maintain pointer, length and the have
        """
        if self.right < self.sLength - 1:
            self.right += 1
            self._updateLength()
            self._updateHaveAdd(self.s[self.right])
            return True
        return False
        """
            shrink ; maintain pointer, length and the have
        """
    def shrink(self)->bool:
        if self.left < self.right:
            self._updateHaveRemove(self.s[self.left])
            self.left += 1
            self._updateLength()
            return True
        return False    

    def process_special(self)->str:
        """
            returns empty string if both s, t are not 
            if length of t is 1 ... it will check if t is in s and return "t" if it exists
            returns None if it is not special case
        """
        if not self.s or not self.t:
            return ""
        if len(self.t) == 1:
            if self.t in self.s:
                return self.t
            else:
                return None
        return None

class Result:
    def __init__(self):
        self.length = float('inf')
        self.s = ""

    def update(self, s: str):
        if len(s) < self.length:
            self.length = len(s)
            self.s = s

def  minWindow(s: str, t: str) -> str:

    w: Window = Window(s, t)
    
    special = w.process_special()
    if special is not None:
        return special
    res: Result = Result()
    while w.expand():
        if w.matches():
            res.update(w.wind())
            while(w.shrink()):
                if w.matches():
                    res.update(w.wind())
                else:
                    break
    return res.s

# ------------------------------------------------------------------
# Test Harness
# ------------------------------------------------------------------
def run_tests(func):
    test_cases = [
        ("Breaking Case 1: Empty String s", "", "a", ""),
        ("Breaking Case 2: Matching at start", "a", "a", "a"),
    ]

    print(f"\nRunning tests for: {func.__name__}\n")
    passed = 0
    for desc, s, t, expected in test_cases:
        try:
            print(f"Testing {desc} with s='{s}', t='{t}'")
            result = func(s, t)
            if result == expected:
                print(f"✅ {desc}: Passed")
                passed += 1
            else:
                print(f"❌ {desc}: Failed")
                print(f"   Input: s={s}, t={t}")
                print(f"   Expected: '{expected}'")
                print(f"   Actual:   '{result}'")
        except Exception as e:
            print(f"❌ {desc}: CRASHED with Error: {e}")
        print("-" * 30)
    print(f"\n{passed}/{len(test_cases)} passed\n")

run_tests(minWindow)

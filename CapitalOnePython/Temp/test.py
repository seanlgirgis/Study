from collections import Counter
import sys
"""
    LeetCode 76. Minimum Window Substring
    
    Given strings s and t, return the minimum window in s which will contain all the characters in t.
    
    Solution Approach: -
        OOP. Use Object Window and Object Result
        Class Result it keeps Track of the minimum possible solution
        Class Window
            Keeps Track off
                Counter of the target string and main string to search in
                keeps track of its length and its starting index and ending index
                systematically changes left and right pointer as it expands or shrinks  while updating the Counter of the have .. need is fixed
                Behaviour: -
                    A) systematically maintains window length
                    B) updates the have dictionary with adds to right and removes at left
                    C) calculates matches between the need and have 
                    D) it can process special for cases of "" or a single letter to search for
                    E) It shrinks and expands maintaining that it never exceed the string limits. 
                        While changing its size and position, it updates let and right pointer,
                            the winfow length, the have Counter
    
"""
        
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

    def process_special(s: str, t: str)->str:
        """
            returns empty string if both s, t are not 
            if length of t is 1 ... it will check if t is in s and return "t" if it exists
            returns None if it is not special case
        """
        if len(t) > len(s):
            return ""   
        if not t:  
            return ""
        if not s:  
            return ""
        if len(t) == 1:
            if t in s:
                return t
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
    special = Window.process_special(s, t)
    if special is not None:
        return special

    w: Window = Window(s, t)

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
#print("ADOBECODEBANC" , "ABC", "Output ", minWindow ("ADOBECODEBANC" , "ABC"))
#print("cabwefgewcwaef" , "cae", "Output ", minWindow ("cabwefgewcwaef" , "cae"))
print("ab", "ab", "Expected: ab, Got:", minWindow("ab", "ab"))
print("XabcYdefZabc", "abc", "Expected: abc, Got:", minWindow("XabcYdefZabc", "abc"))
print("aXbYcZdefabc", "abc", "Expected: abc, Got:", minWindow("aXbYcZdefabc", "abc"))
print("abacaba", "aba", "Expected: aba, Got:", minWindow("abacaba", "aba"))
print("aaabcdeffabc", "abc", "Expected: abc, Got:", minWindow("aaabcdeffabc", "abc"))
print("cwaefg", "cae", "Expected: cwae, Got:", minWindow("cwaefg", "cae"))  # already passed
print("cwaefgX", "cae", "Expected: cwae, Got:", minWindow("cwaefgX", "cae"))
print("ADOBECODEBAN", "ABC", "Expected: BANC, Got:", minWindow("ADOBECODEBAN", "ABC"))
print("ADOBECODEBANCX", "ABC", "Expected: BANC, Got:", minWindow("ADOBECODEBANCX", "ABC"))
print("bbba", "ab", "Expected: ba, Got:", minWindow("bbba", "ab"))
print("aabbcc", "abc", "Expected: aabbcc, Got:", minWindow("aabbcc", "abc"))  # whole string needed
print("", "abc", "Expected: '', Got:", minWindow("", "abc"))
print("abc", "", "Expected: '', Got:", minWindow("abc", ""))


sys.exit()
print("", "a", "Expected: '', Got:", minWindow("", "a"))
print("a", "aa", "Expected: '', Got:", minWindow("a", "aa"))
print("a", "b", "Expected: '', Got:", minWindow("a", "b"))
print("abc", "b", "Expected: b, Got:", minWindow("abc", "b"))
print("abc", "ac", "Expected: abc, Got:", minWindow("abc", "ac"))
print("aa", "aa", "Expected: aa, Got:", minWindow("aa", "aa"))
print("ADOBECODEBANC", "ABC", "Expected: BANC, Got:", minWindow("ADOBECODEBANC", "ABC"))
print("a", "a", "Expected: a, Got:", minWindow("a", "a"))
print("a", "a", "Expected: a, Got:", minWindow("a", "a"))
# Match at position 0 with shorter window than full string
print("ab", "a", "Expected: a, Got:", minWindow("ab", "a"))

# Match is the very first character
print("aXYZ", "a", "Expected: a, Got:", minWindow("aXYZ", "a"))

# Best match is at the start, longer t
print("abcXXXcba", "abc", "Expected: abc, Got:", minWindow("abcXXXcba", "abc"))

# Entire string is the answer and match exists from first expansion
print("ba", "ab", "Expected: ba, Got:", minWindow("ba", "ab"))

# Single char s and t that match (without process_special saving it)
print("ab", "ab", "Expected: ab, Got:", minWindow("ab", "ab"))
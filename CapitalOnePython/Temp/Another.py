from collections import Counter

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
        self.satisfied = 0
        self.need_count = len(self.need)
        self._updateHaveAdd(s[0])

    def _getEmptyHave(self) -> Counter:
        return Counter({key: 0 for key in self.need})

    def _updateLength(self):
        self.length = self.right - self.left + 1

    def _updateHaveAdd(self, ch: str) -> None:
        if ch in self.have:
            self.have[ch] += 1
            if self.have[ch] == self.need[ch]:
                self.satisfied += 1

    def _updateHaveRemove(self, ch: str) -> None:
        if ch in self.have:
            if self.have[ch] == self.need[ch]:
                self.satisfied -= 1
            self.have[ch] -= 1

    def matches(self) -> bool:
        return self.satisfied == self.need_count

    def wind(self) -> str:
        return self.s[self.left:self.right + 1]

    def expand(self) -> bool:
        if self.right < self.sLength - 1:
            self.right += 1
            self._updateLength()
            self._updateHaveAdd(self.s[self.right])
            return True
        return False

    def shrink(self) -> bool:
        if self.left < self.right:
            self._updateHaveRemove(self.s[self.left])
            self.left += 1
            self._updateLength()
            return True
        return False

    def process_special(s: str, t: str) -> str:
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


def minWindow(s: str, t: str) -> str:
    special = Window.process_special(s, t)
    if special is not None:
        return special

    w = Window(s, t)
    res = Result()

    while w.expand():
        if w.matches():
            res.update(w.wind())
            while w.shrink():
                if w.matches():
                    res.update(w.wind())
                else:
                    break
    return res.s







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
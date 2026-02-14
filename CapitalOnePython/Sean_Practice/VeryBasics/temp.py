from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Compress the character array in-place according to the following rules:
        - Each group of consecutive identical characters is replaced by the character
          followed by the count of the group if the count > 1.
        - The compression is done in-place and the function returns the new length.

        Time: O(n), Space: O(1) extra space
        """
        if not chars:
            return 0

        self.chars = chars
        self.n = len(chars)
        self.write = 0           # current position to write next character/count
        self.group_start = 0     # start index of current group
        self.current_char = chars[0]

        for i in range(self.n):
            if chars[i] != self.current_char:
                self._write_group(i)
                self.group_start = i
                self.current_char = chars[i]

        # Don't forget to write the last group
        self._write_group(self.n)

        return self.write

    def _write_group(self, end: int) -> None:
        """
        Write the current group (from group_start to end-1) starting at self.write.
        Updates self.write accordingly.
        """
        count = end - self.group_start

        # Write the character
        self.chars[self.write] = self.current_char
        self.write += 1

        # Write the count only if > 1
        if count > 1:
            for digit in str(count):
                self.chars[self.write] = digit
                self.write += 1


# ────────────────────────────────────────────────────────────────
#                          Test Harness
# ────────────────────────────────────────────────────────────────

def run_tests() -> None:
    test_cases: list[tuple[list[str], int, list[str]]] = [
        # 1 Empty
        ([], 0, []),
        # 2 Single
        (["a"], 1, ["a"]),
        # 3 First single
        (["a", "b", "b", "c"], 4, ["a", "b", "2", "c"]),
        # 4 Last single
        (["a", "a", "b", "c"], 4, ["a", "2", "b", "c"]),
        # 5 All singles
        (["a", "b", "c", "d"], 4, ["a", "b", "c", "d"]),
        # 6 All same
        (["z", "z", "z", "z"], 2, ["z", "4"]),
        # 7 Standard
        (["a", "a", "b", "b", "c", "c", "c"], 6, ["a", "2", "b", "2", "c", "3"]),
        # 8 Exactly 2
        (["x", "x"], 2, ["x", "2"]),
        # 9 Exactly 9
        (["x"] * 9, 2, ["x", "9"]),
        # 10 Ten
        (["y"] * 10, 3, ["y", "1", "0"]),
        # 11 Twelve
        (["m"] * 12, 3, ["m", "1", "2"]),
        # 12 Multiple large groups
        (["a"] * 10 + ["b"] * 15 + ["c"] * 20, 9, ["a", "1", "0", "b", "1", "5", "c", "2", "0"]),
        # 13 Alternating
        (["a", "b", "a", "b", "a", "b"], 6, ["a", "b", "a", "b", "a", "b"]),
        # 14 Two large consecutive
        (["p"] * 11 + ["q"] * 11, 6, ["p", "1", "1", "q", "1", "1"]),
        # 15 Single in middle
        (["a", "a", "b", "c", "c"], 5, ["a", "2", "b", "c", "2"]),
        # 16 Groups with single in middle
        (["x", "x", "y", "z", "z"], 5, ["x", "2", "y", "z", "2"]),
    ]

    sol = Solution()

    for idx, (input_chars, expected_len, expected_chars) in enumerate(test_cases, 1):
        # Make a copy because we modify in-place
        chars_copy = input_chars[:]
        length = sol.compress(chars_copy)

        passed = (length == expected_len) and (chars_copy[:length] == expected_chars)

        status = "PASS" if passed else "FAIL"
        print(f"Test {idx:2d} {status}")
        if not passed:
            print(f"  Got length: {length}, expected: {expected_len}")
            print(f"  Got array : {chars_copy[:length]}")
            print(f"  Expected  : {expected_chars}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
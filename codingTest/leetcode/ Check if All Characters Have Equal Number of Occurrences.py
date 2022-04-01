 import py


# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
# Check if All Characters Have Equal Number of Occurrences.py


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        c = Counter(s).most_common()
        if c[0][1] != c[-1][1]:
            return False
        return True
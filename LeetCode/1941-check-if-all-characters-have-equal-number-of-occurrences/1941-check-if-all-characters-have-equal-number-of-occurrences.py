

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        c = Counter(s).most_common()
        if c[0][1] != c[-1][1]:
            return False
        return True
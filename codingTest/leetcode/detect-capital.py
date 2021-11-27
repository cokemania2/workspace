# https://leetcode.com/problems/detect-capital/submissions/
# detect-capital.py


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if (word.upper() == word or
            word.capitalize() == word or
            word.lower() == word):
                return True
        return False
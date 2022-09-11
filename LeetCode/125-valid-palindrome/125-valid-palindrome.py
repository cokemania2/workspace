import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return True if res == res[::-1] else False
            
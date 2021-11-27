# https://leetcode.com/problems/rotate-string/
# Rotate String.py

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_length = len(s)
        for i in range(s_length):
            print(s[i:] + s[:i])
            if s[i:] + s[:i] == goal:
                return True
        return False
# https://leetcode.com/problems/reformat-the-string
# Reformat The String.py

class Solution:
    def reformat(self, s: str) -> str:
        st = ""
        a = []
        b = []
        for i, v in enumerate(s):
            if v.isdigit():
                a.append(v)
            else:
                b.append(v)
        if len(a) < len(b):
            a, b = b, a
        if len(a) >= len(b) + 2:
            return st
        for i in range(len(a)+len(b)):
            if i % 2 == 0:
                st += a.pop()
            else:
                st += b.pop()
        return st
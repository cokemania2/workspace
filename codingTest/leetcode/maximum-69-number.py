# https://leetcode.com/problems/maximum-69-number/submissions/
# maximum-69-number.py

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        for i,v in enumerate(s):
            if v == '6':
                s[i] = '9'
                break
        return int(''.join(s))
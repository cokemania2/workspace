# https://leetcode.com/problems/roman-to-integer/
# roman-to-integer.py

class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        flag = False
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(1, len(s)):
            if flag:
                flag = False
                continue
            a = dic[s[i-1]]
            b = dic[s[i]]
            if b > a:
                answer += b - a
                flag = True
            else:
                answer += a
        last = dic[s[len(s)-1]]
        answer += last if not flag else 0
        return answer
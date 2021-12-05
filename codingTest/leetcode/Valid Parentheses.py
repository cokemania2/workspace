# https://leetcode.com/problems/valid-parentheses/
# Valid Parentheses.py

class Solution:
    def useStack(self, s):
        dic = {'}':'{',']':'[',')':'('}
        stack = []
        for i in s:
            if i in dic.keys():
                if len(stack) != 0 and dic[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if len(stack) == 0 else False
    
    def isValid(self, s: str) -> bool:
        return self.useStack(s)
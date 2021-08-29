# https://programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호.py

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        elif i ==')' and len(stack) !=0 and stack[-1] == '(':
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False
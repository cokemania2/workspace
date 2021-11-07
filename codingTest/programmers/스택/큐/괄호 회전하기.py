# https://programmers.co.kr/learn/courses/30/lessons/76502#
# 괄호 회전하기.py

def is_right_string(s):
    dict = {'}':'{',')':'(',']':'['}
    stack = []
    for i in s:
        if i in ['[','{','(']:
            stack.append(i)
        elif len(stack) != 0 and dict[i] == stack[-1]:
            stack.pop()
        else:
            return False
    return (True if len(stack) == 0 else False)
                    
def solution(s):
    answer = 0
    
    for i in range(1,len(s)):
        if is_right_string(s[-i:]+s[:len(s)-i]):
            answer += 1
    
    return answer + (1 if is_right_string(s) else 0)
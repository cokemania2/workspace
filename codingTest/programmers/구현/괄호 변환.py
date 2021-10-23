# https://programmers.co.kr/learn/courses/30/lessons/60058
# 괄호 변환.py


def split_uv(p):
    stack = []
    left = 0
    right = 0
    for i,v in enumerate(p):
        if v == '(':
            stack.append(v)
            left += 1
        else:
            right += 1
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
        if left == right:
            print(p[:i+1], p[i+1:])
            if len(stack) == 0:
                return p[:i+1] +  split_uv(p[i+1:])
            else:
                s = '(' + split_uv(p[i+1:]) + ')'
                for j in range(1, i):
                    s += '(' if p[j] == ')' else ')'
                return s
    return p
                
            
def solution(p):
    if len(p) == 0:
        return ''
    return split_uv(p)
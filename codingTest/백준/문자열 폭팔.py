# https://www.acmicpc.net/problem/9935
# 문자열 폭팔.py

def boom(s, bomb):
    stack = []
    for i in s:
        stack.append(i)
        if "".join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]
    return "".join(stack) if len(stack) != 0 else "FRULA"

s = input()
bomb = input()
print(boom(s,bomb))

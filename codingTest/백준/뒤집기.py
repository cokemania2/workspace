# https://www.acmicpc.net/problem/1439
# 뒤집기.py

stack = []
s = input()
for i in s:
    if len(stack) != 0 and stack[-1] == i:
        continue
    stack.append(i)
print(min(stack.count('1'), stack.count('0')))
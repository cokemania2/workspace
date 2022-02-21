# https://www.acmicpc.net/problem/1406
# 에디터.py

import sys
s = input()
m = int(input())
cursor = len(s)
for i in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        cursor -= 1 if cursor > 0 else 0
    elif command[0] == 'D':
        cursor += 1 if cursor < len(s)  else 0
    elif command[0] == 'B':
        if cursor == 0:
            continue
        s = s[:cursor-1] + s[cursor:]
        cursor -= 1 if cursor > 0 else 0
    elif command[0] == 'P':
        if cursor == 0:
            s = command[1] + s
        else:
            s = s[:cursor] + command[1] + s[cursor:]
        cursor += 1
print(s)
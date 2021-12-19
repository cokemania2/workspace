# https://www.acmicpc.net/problem/3028
# 창영마을.py

s  = input()
now = 1
for i in s:
    if i == 'A':
        if now == 1:
            now = 2
        elif now == 2:
            now = 1
    elif i == 'B':
        if now == 2:
            now = 3
        elif now == 3:
            now = 2
    else:
        if now == 3:
            now = 1
        elif now == 1:
            now = 3
print(now)
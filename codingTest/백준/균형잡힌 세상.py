# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상.py

while True:
    s = list(input())
    if s[0] == '.' and len(s) == 1:
        break
    a = []
    for i in s:
        if i == '[':
            a.append(i)
        elif i == ']':
            if len(a) ==0 or len(a) != 0 and a[-1] != '[':
                a.append(i)
                break
            a.pop()
        elif i == '(':
            a.append(i)
        elif i == ')':
            if len(a) ==0 or len(a) != 0 and a[-1] != '(':
                a.append(i)
                break
            a.pop()
    if len(a) == 0:
        print('yes')
    else:
        print('no')

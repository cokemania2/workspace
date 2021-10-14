# https://www.acmicpc.net/problem/9012
# 괄호.py

def check_vps(w):
    n_list = []
    for n in w:
        if n == '(':
            n_list.append(n)
        else:
            if len(n_list) == 0 or n_list.pop() != '(':
                print('NO')
                return
    if len(n_list) == 0:
        print('YES')
    else:
        print('NO')

T = int(input())
for i in range(T):
    w =   list(input())
    check_vps(w)
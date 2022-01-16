# https://www.acmicpc.net/problem/16435
# 스네이크버드.py

N, L = map(int, input().split())
food = list(sorted(list(map(int,input().split()))))
for i in food:
    if i <= L:
        L += 1
    else:
        break
print(L)

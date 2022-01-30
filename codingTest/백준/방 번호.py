# https://www.acmicpc.net/problem/1475
# 방 번호.py

N = input()
nList = []
n69 = 0
for i in range(0,10):
    if i == 6 or i == 9:
        n69 += N.count(str(i))
        continue
    nList.append(N.count(str(i)))
n69 = n69 // 2 + (0 if n69 % 2 == 0 else 1)
print(max(n69,max(nList)))

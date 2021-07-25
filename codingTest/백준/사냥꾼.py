# 사냥꾼.py
# https://www.acmicpc.net/problem/8983
# 사대의 위치를 먼저 기록하고, 동물들의 위치를 기준으로 사대의 영역에 포함되는지를 확인하는 방식으로 풀었다

answer = 0
M, N ,L = map(int,input().split())
X = sorted(list(map(int,input().split())))
xlist = [False]*(X[-1]+L+1)
for i in X :
    xlist[i] = True
for i in range(N) :
    x, y = map(int,input().split())
    if xlist[x]  and y <= L :
        answer += 1
        continue
    for j in range(1,L+1) :
        if (x+j < len(xlist) and xlist[x+j]  or x-j >=0 and xlist[x-j] ) and L-j >= y  :
            answer += 1
            break
print(answer)

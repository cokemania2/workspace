##https://www.acmicpc.net/problem/10810
##공넣기
## 4m 49s

N, M = map(int,input().split())
arr = [0 for _ in range(N)]
for i in range(M) :
    i ,j, k = map(int,input().split())
    for x in range(i, j + 1) :
        arr[x -1] = k
for i in arr :
    print(i,end=' ')
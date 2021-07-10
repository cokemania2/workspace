##https://www.acmicpc.net/problem/10569
##다면체
## 2m 11s

T = int(input())
for i in range(T) :
    V ,E = map(int,input().split())
    print(E - V + 2)

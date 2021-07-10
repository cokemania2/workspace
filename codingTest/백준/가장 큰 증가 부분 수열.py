##https://www.acmicpc.net/problem/11055
##가장 큰 증가 부분 수열

##리스트를 반대로 돌려서 가장 큰 감소 부분수열을 구했다.
##자신(i)의 위치에서 뒤에 있는 원소들(j)과 비교하며
##나보다 큰것들 중에 제일 큰 dp값을 내 자신에 더해서(dp.append)
##마지막에 dp들중에 제일 큰값을 출력했다.

N = int(input())
arr = list(reversed(list(map(int,input().split()))))
dp = [arr[0]]
for i in range(1,N) :
    maxx = 0
    for j in range(i) :
        if arr[j] > arr[i] and dp[j] > maxx:
            maxx = dp[j]
    dp.append(arr[i] + maxx)
print(max(dp))
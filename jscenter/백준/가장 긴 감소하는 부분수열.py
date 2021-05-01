##https://www.acmicpc.net/problem/11722
##가장 긴 감소하는 부분 수열 

N = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1]
for i in range(1,N) :
    maxx = 0
    maxj = 0
    for j in range(i) :
        if arr[j] < arr[i] and dp[j] > maxx :
            maxj = j
            maxx = dp[j]
    if maxx == 0 :
        dp.append(1)
    else :
        dp.append(1 + dp[maxj])
print(max(dp))
# 1로 만들기.py
# https://www.acmicpc.net/submit/1463/31700545
# 1부터 N까지 나아가면서 i까지의 최단 거리를 구해주면 된다.

N = int(input())
dp = [0,0]
for i in range(2,N+1) :
    dp.append(dp[i-1] + 1)
    if i%3 == 0 :
        dp[i] = min(dp[i//3] + 1,dp[i])
    if i % 2 == 0 :
        dp[i] = min(dp[i//2] + 1,dp[i])
print(dp[N])
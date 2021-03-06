##https://www.acmicpc.net/problem/11726
##2xn 타일링

N = int(input())
dp = [0,1,3,5]
for i in range(4,N+1) :
    dp.append(dp[i -1]  + dp[i-2] * 2)
print(dp[N] % 10007)
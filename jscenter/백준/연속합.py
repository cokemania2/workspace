##https://www.acmicpc.net/problem/1912
##연속 합

##n = int(input())
##ls = list(map(int,input().split(' ')))
##maxx = -1001
##for i in range (1, n + 1) :
##    for j in range(0, n) : # 시작, 끝, 늘어나는 수
##        if sum(ls[j:j+i]) > maxx :
##            maxx = sum(ls[j:j+i])
##print(maxx)

n = int(input())
ls = list(map(int,input().split(' ')))
dp = []
dp.append(ls[0])
for i in range(1, n) :
    if ls[i] + dp[i - 1] > ls[i] :
        dp.append(ls[i] + dp[i -1])
    else :
        dp.append(ls[i])
print(max(dp))
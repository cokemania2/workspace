# https://programmers.co.kr/learn/courses/30/lessons/43105
# 정수삼각형.py

def solution(triangle):
    
    length = len(triangle)
    triangle = list(reversed(triangle))
    dp = [[] for _ in range(length)]
    dp[0] = triangle[0]
    for i in range(1, length):
        for j in range(len(triangle[i])):
            dp[i].append(max(dp[i-1][j],dp[i-1][j+1]) + triangle[i][j])
    return dp[-1][0]
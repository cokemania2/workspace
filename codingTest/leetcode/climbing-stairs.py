# https://leetcode.com/problems/climbing-stairs/
# climbing-stairs.py

class Solution: 
    def climbStairs(self, n: int) -> int:
        dp = [1, 2, 3]
        for i in range(3, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n-1]
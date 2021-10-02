# https://leetcode.com/problems/first-bad-version/
# first-bad-version.py

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        return self.findBadVersion(1,n,n//2)
    def findBadVersion(self, a, b, n):
        if a > b or not isBadVersion(n-1) and isBadVersion(n):
            return n
        else:
            if not isBadVersion(n-1):
                a = n + 1
            else:
                b = n - 1 
            n = a + (b-a) // 2
            return self.findBadVersion(a, b, n)
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def binarysearch(self, n):
        answer, left, right = 0, 1, n
        while True:
            mid = (left + right) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
                answer = mid
            if left > right:
                return answer

    def firstBadVersion(self, n: int) -> int:
        return self.binarysearch(n)
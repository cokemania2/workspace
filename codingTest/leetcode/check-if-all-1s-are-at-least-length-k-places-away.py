# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# check-if-all-1s-are-at-least-length-k-places-away.py

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        first = True
        stack = []
        for i,num in enumerate(nums):
            if num == 0:
                stack.append(num)
            else:
                if first:
                    first = False
                elif len(stack) < k:
                    return False
                stack = []
        return True

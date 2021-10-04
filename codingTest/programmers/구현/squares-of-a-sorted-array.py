# https://leetcode.com/problems/squares-of-a-sorted-array
# squares-of-a-sorted-array.py


def pow2(a):
    return pow(a,2)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(pow2,nums)))
# https://leetcode.com/problems/search-insert-position/
# search-insert-position.py

from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
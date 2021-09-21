# https://leetcode.com/problems/binary-search/submissions/
# binary-search.py

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = len(nums) // 2
        while(l <= r):
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            mid = l + (r - l) // 2
        return -1
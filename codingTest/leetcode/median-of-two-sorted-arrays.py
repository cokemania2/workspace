# https://leetcode.com/problems/median-of-two-sorted-arrays
# median-of-two-sorted-arrays.py

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = list(sorted(nums1 + nums2))
        if len(nums) % 2 == 0:
            return float((nums[len(nums)//2] + nums[len(nums)//2-1])/2)
        else:
            return float(nums[(len(nums)//2)])
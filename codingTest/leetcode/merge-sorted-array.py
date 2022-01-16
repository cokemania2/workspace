# https://leetcode.com/problems/merge-sorted-array/
# merge-sorted-array.py

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i, num in enumerate(nums2):
            nums1[-(i+1)] = num
        nums1.sort()
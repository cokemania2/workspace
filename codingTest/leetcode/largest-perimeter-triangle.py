# https://leetcode.com/problems/largest-perimeter-triangle/submissions/
# largest-perimeter-triangle.py

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums,reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return sum(nums[i:i+3])
        return 0
            
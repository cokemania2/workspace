import math

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return max(math.prod(nums[:3]), nums[-1] * nums[-2] * nums[0])
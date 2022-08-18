class Solution:
    def binarysearch(self, nums, target):
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(nums, target)
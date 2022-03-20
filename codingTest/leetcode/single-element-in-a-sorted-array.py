# https://leetcode.com/problems/single-element-in-a-sorted-array/
# single-element-in-a-sorted-array.py

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        before = nums[0]
        flag = True
        for i in range(1, len(nums)):
            if nums[i] != before:
                if flag:
                    return before
                else:
                    before = nums[i]
                    flag = True
            else:
                flag = False
        return before
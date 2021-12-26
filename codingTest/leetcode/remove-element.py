# https://leetcode.com/problems/remove-element/
# remove-element.py

class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        
        def change_ab(nums, a, b):
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp
            
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                for j in range(i+1, length):
                    if nums[j] != val and nums[i] != nums[j]:
                        change_ab(nums, i,j)       
                        
        return length - nums.count(val)
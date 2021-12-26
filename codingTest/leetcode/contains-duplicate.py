# https://leetcode.com/problems/contains-duplicate/submissions/
# contains-duplicate.py

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
# https://leetcode.com/problems/move-zeroes
# move-zeroes.py

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        answer = []
        for num in nums:
            if num != 0:
                answer.append(num)
        answer += [0 for _ in range(len(nums)-len(answer))]
        nums[:] = answer[:]
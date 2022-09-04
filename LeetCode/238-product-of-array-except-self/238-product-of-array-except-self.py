class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        left_arr = [1, nums[0]]
        right_arr = [1, nums[-1]]
        length = len(nums)
        for i in range(1, length):
            left_arr.append(nums[i] * left_arr[-1])
            right_arr.append(nums[-i-1] * right_arr[-1])
        for i in range(length):
            answer.append(left_arr[i] * right_arr[length-i-1])
        return answer

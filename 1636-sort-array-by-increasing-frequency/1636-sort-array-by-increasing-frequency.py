class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = {}
        set_nums = set(nums)
        for i in set_nums:
            dic[i] = nums.count(i)
        nums.sort(key=lambda x : (dic[x], -x))

        return nums
        
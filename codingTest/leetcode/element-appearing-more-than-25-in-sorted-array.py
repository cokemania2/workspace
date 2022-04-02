# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# element-appearing-more-than-25-in-sorted-array.py

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        before = 0
        count = 1
        max_count = 1
        max_i = arr[0]
        for i in arr:
            if i == before:
                count += 1
                if count > max_count:
                    max_count = count
                    max_i = i
            else:
                count = 1
            before = i
        return max_i
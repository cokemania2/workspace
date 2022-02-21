# mean-of-array-after-removing-some-elements.py
# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        split = len(arr)//20
        return sum(arr[split:-split]) / (len(arr) - (2*split))
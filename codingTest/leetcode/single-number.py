# https://leetcode.com/problems/single-number/submissions/
# single-number.py

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]
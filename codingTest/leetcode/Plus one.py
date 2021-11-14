# https://leetcode.com/problems/plus-one/
# Plus one.py

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int("".join(list(map(str,digits)))) + 1))
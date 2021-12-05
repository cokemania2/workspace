https://leetcode.com/problems/consecutive-characters/
consecutive-characters.py

class Solution:
    def maxPower(self, s: str) -> int:
        before = ""
        count = 1
        maxx = 0
        for i in s:
            if i == before:
                count += 1
            else:
                if count > maxx:
                    maxx = count
                count = 1
            before = i
        return max(maxx,count)

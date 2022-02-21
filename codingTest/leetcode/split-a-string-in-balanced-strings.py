# https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Split a String in Balanced Strings.py

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = count = 0
        for i in s:
            count += 1 if i == 'L' else -1
            answer += 1 if count == 0 else 0
        return answer
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/
# largest-substring-between-two-equal-characters.py

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        answer = []
        alpha ={}
        for i, v in enumerate(s):
            if v in alpha:
                answer.append(i - alpha[v] - 1)
            else:
                alpha[v] = i
        answer = max(answer) if len(answer) != 0 else -1
        return answer
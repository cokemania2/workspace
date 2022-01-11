# https://leetcode.com/problems/adding-spaces-to-a-string/submissions/
# adding-spaces-to-a-string.py

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ''
        front = 0
        for space in spaces:
            answer += s[front:space] + ' '
            front = space
        return answer + s[spaces[-1]:]
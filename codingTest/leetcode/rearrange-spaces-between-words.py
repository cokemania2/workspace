# https://leetcode.com/problems/rearrange-spaces-between-words/
# rearrange-spaces-between-words.py

class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_count = text.count(' ')
        word_count = len(text.split())
        if word_count == 1:
            return text.split()[0] + ' '*space_count
        s = space_count // (word_count - 1)
        return ((' ' * s).join(text.split())) + (' ' * (space_count % (word_count - 1)))
        
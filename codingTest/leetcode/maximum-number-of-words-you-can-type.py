# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
# maximum-number-of-words-you-can-type.py

class Solution:
    def check(self, brokenLetters, word):
        for i in brokenLetters:
            if i in word:
                return False
        return True
                    
    
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        answer = 0
        text = text.split()
        brokenLetters = list(brokenLetters)
        for word in text:
            if self.check(brokenLetters, word):
                answer += 1
        return answer
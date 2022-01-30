# https://leetcode.com/problems/keyboard-row/
# keyboard-row.py

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def can_one_row(word):
            x = ["QWERTYUIOP", "ASDFGHJKL","ZXCVBNM"]
            for row in x:
                flag = True
                for w in word:
                    if w not in row:
                        flag = False
                        break
                if flag:
                    return True
            return False
        
        answer = []
        for word in words:
            if can_one_row(word.upper()):
                answer.append(word)
        return answer
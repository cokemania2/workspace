# https://leetcode.com/problems/construct-the-rectangle/submissions/
# construct-the-rectangle.py

class Solution:
    def constructRectangle(self, area: int) -> List[int]:     
        answer = []      
        
        for i in range(1,(area+1)//2 + 1):
            if area % i == 0:
                answer.append([area//i, i])
        answer.sort(key = lambda x : abs(x[0]-x[1]))
        return answer[0]
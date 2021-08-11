# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/submissions/
# maximum-points-you-can-obtain-from-cards.py

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        answer = 0
        ldp = [cardPoints[0]] +[0] * (k-1)
        rdp = [cardPoints[-1]] + [0] * (k-1)
        for i in range(1, k):
            ldp[i] = ldp[i-1] + cardPoints[i]
            rdp[i] = rdp[i-1] + cardPoints[-(i+1)]
        for i in range(k-1) :
            answer = max(answer,ldp[i] + rdp[k-2-i])
        return max(answer,max(ldp[k-1], rdp[k-1]))
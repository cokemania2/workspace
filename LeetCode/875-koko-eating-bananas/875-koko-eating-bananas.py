class Solution:
    def timeSpent(self, piles, kh):
        return sum([pile // kh + (0 if pile % kh == 0 else 1)  for pile in piles])
    
    def binarySearch(self, piles, h):
        left = 1
        answer = right = piles[-1]
        while left <= right:
            mid = (left + right) // 2
            spent_time = self.timeSpent(piles, mid)
            if spent_time <= h:
                answer = min(answer, mid)
                right = mid - 1
            else:
                left = mid + 1
        return answer
            
        
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        return self.binarySearch(piles, h)
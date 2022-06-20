class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # 홀수갯수 vs 짝수갯수 한다음에 더 작은것이 움직이도록
        a, b = 0, 0
        for i in position:
            if i % 2 == 0:
                a += 1
            else:
                b += 1
        return min(a, b)
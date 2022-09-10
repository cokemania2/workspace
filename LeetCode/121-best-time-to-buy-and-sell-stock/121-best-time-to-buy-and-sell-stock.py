import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = prices[0], 0
        for price in prices: 
            if price < minPrice:
                minPrice  = price
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit
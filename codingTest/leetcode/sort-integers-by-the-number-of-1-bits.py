# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits
# sort-integers-by-the-number-of-1-bitssort-integers-by-the-number-of-1-bits.py

# python은 bin(x) 가 있다.. 잊지말자 

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countOneBit(n):
            stack = []
            while n > 1:
                stack.append(n % 2)
                n //= 2
            stack.append(n)
            return stack.count(1)
        
        return list(sorted(arr, key = lambda x : (countOneBit(x), x)))
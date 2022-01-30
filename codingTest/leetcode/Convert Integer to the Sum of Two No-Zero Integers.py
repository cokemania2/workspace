# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
# Convert Integer to the Sum of Two No-Zero Integers.py

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(s):
            if str(s).find('0') == -1:
                return True
            return False
        for i in range(1, n):
            if check(i) and check(n-i):
                return [i, n-i]
# number-of-steps-to-reduce-a-number-to-zero.py
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        answer = 0
        while True:
            if num == 0:
                return answer
            elif num % 2 == 1:
                num -= 1
            else:
                num /= 2
            answer += 1
                
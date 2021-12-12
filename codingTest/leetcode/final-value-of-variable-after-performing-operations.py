# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# final-value-of-variable-after-performing-operations.py

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for op in operations:
            answer += (1 if op[0] == '+' or op[-1] == '+' else -1)
        return answer
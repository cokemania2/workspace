class Solution(object):
    def dfs(self, candidates, target, result, answer):
        if target < 0:
            return
        if target == 0:
            answer.append(result)
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target-candidates[i], result+[candidates[i]], answer)
        
    def combinationSum(self, candidates, target):
        answer = []
        self.dfs(candidates, target, [], answer)
        return answer
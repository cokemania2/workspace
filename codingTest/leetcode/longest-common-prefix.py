# longest-common-prefix.py
# https://leetcode.com/problems/longest-common-prefix/submissions/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        for i in range(len(pivot)) :
            for j in range(len(strs)) :
                if pivot[:i+1] == strs[j][:i+1] :
                    continue
                else :
                    return pivot[:i]
        return pivot
    
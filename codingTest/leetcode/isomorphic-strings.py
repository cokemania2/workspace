# https://leetcode.com/problems/isomorphic-strings/submissions/
# isomorphic-strings.py

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        used = {}
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                dic[s[i]] = t[i]
                used[t[i]] = True
        
        return True
            
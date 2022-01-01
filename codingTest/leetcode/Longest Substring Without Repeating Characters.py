# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Longest Substring Without Repeating Characters.py

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        maxx = 0
        for i in range(length):
            dic = {}
            dic[s[i]] = True
            cnt = 1
            for j in range(i+1, length):
                if s[j] in dic:
                    maxx = max(maxx, cnt)
                    break
                else:
                    dic[s[j]] = True
                    cnt += 1
            maxx = max(maxx, cnt)
        return maxx
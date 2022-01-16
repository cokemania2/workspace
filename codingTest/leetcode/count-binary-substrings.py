# https://leetcode.com/problems/count-binary-substrings/
# count-binary-substrings.py

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        def check_substring(a, b, s):
            count = 0
            before_a = s[a]
            before_b = s[b]
            while a >= 0 and b < len(s):
                if s[a] != s[b] and s[a] == before_a and s[b] == before_b:
                    count += 1
                    a -= 1
                    b += 1
                else:
                    break
            return count
            
        answer = 0
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                answer += check_substring(i-1, i,s)
        return answer
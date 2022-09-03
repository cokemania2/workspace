class Solution:
    def sortStr(self, s):
        return ''.join(sorted(list(s)))
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedList = sorted(enumerate(list(map(self.sortStr,strs))), key=lambda x:x[1])
        answer = [[strs[sortedList[0][0]]]]
        for i in range(1, len(sortedList)):
            if sortedList[i][1] == sortedList[i-1][1]:
                answer[-1].append(strs[sortedList[i][0]])
            else:
                answer.append([strs[sortedList[i][0]]])
        return answer
            
            
# https://leetcode.com/problems/count-items-matching-a-rule/
# count-items-matching-a-rule.py

class Solution:

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        class Rule:
            def __init__(self):
                self.typedict = {}
                self.colordict = {}
                self.namedict = {}
                
            def change_dic(self, key):
                if key == 'type':
                    dic = self.typedict
                if key == 'color':
                    dic = self.colordict                
                if key == 'name':
                    dic = self.namedict
                return dic   

            def insert(self, key, item):
                dic = self.change_dic(key)
                if item in dic:
                    dic[item] += 1
                else:
                    dic[item] = 1                   
        
            def find(self, k, v):
                dic = self.change_dic(k)
                return dic[v] if v in dic else 0
        

            
        rule = Rule()    
        
        for i, item in enumerate(items):
            rule.insert('type', item[0])
            rule.insert('color', item[1])
            rule.insert('name', item[2])
        return rule.find(ruleKey, ruleValue)
                
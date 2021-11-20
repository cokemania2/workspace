# https://www.acmicpc.net/problem/2754
# 학점 계산.py

dict1 = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0}
dict2 = {'+':0.3, '-':-0.3, '0':0.0}
grade = list(input())
if grade[0] == 'F':
    print('0.0')
else:
    print(dict1[grade[0]]+dict2[grade[1]])
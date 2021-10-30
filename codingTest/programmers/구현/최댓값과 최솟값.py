# https://programmers.co.kr/learn/courses/30/lessons/12939
# 최댓값과 최솟값.py

def solution(s):
    s = list(sorted(list(map(int,s.split()))))
    return str(s[0])+" "+str(s[-1])
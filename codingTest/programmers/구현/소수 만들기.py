# https://programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기.py

from itertools import combinations 

def solution(nums):
    answer = 0
    for i in list(combinations(nums,3)) :
        x = sum(i)
        flag = True
        for i in range (2,x//2) :
            if (x % i == 0) :
                flag = False
                break
        if (flag == True) :
            answer += 1
    return answer
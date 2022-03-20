# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3
# 자릿수 더하기.py

def solution(n):
    answer = 0
    a = list(str(n))
    for i in range (len(a)) :
        answer = answer +int(a[i])
    return answer
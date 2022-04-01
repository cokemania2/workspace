# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3
# 예산.py

def solution(d, budget):
    answer = 0
    now = 0
    
    for i in sorted(d):
        if now + i > budget:
            return answer
        answer += 1
        now += i
    
    return answer
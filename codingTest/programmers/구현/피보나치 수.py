# https://programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수.py

def solution(n):
    answer = 0
    fibo = [0,1,1]
    for i in range(3,n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[-1] % 1234567
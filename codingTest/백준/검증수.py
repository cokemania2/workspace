# https://www.acmicpc.net/problem/2475
# 검증수.py

def fun(n) :
    return int(n)*int(n)

print(sum(list(map(fun,input().split())))%10)
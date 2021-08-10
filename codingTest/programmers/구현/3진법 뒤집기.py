# https://programmers.co.kr/learn/courses/30/lessons/68935
# 3진법 뒤집기.py

def make10to3(n):
    s = []
    while (n>=3):
        s.append(str(n%3))
        n //= 3
    s.append(str(n))
    return "".join(reversed(s))

def make3to10(s):
    ten = 0
    for i,v in enumerate(s):
        ten += int(v) * 3**i
    return ten

def solution(n):
    return make3to10(make10to3(n))
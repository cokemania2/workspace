# https://programmers.co.kr/learn/courses/30/lessons/86491
# 최소직사각형.py

def solution(sizes):  
    sizes = sorted(sizes, key = lambda x : max(x))
    sizes2 = sorted(sizes, key = lambda x : min(x))
    return(max(sizes[-1]) * min(sizes2[-1]))
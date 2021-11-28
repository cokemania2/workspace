# https://programmers.co.kr/learn/courses/30/lessons/77484
# 로또의 최고 순위와 최저 순위.py

def solution(lottos, win_nums):
    answer = []
    n = 0
    v = 0
    for lotto in lottos:
        if lotto == 0:
            v += 1
        if lotto in win_nums:
            n += 1
    if n == 0: # 7등 -> 6등으로 만들기 위한 조건
        n += 1
        v -= 0 if v == 0 else 1
    return [7 - n - v, 7 - n]
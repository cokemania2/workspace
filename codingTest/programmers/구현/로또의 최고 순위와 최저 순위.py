# https://programmers.co.kr/learn/courses/30/lessons/77484
# 로또의 최고 순위와 최저 순위.py

def score_to_rank(p):
    if p <= 1:
        return 6
    if p >= 6:
        return 1
    return (7 - p)

def solution2(lottos, win_nums):
    answer = []
    zero_count = 0
    prize_count = 0
    
    for i in lottos:
        if i == 0:
            zero_count += 1
        elif i in win_nums:
            prize_count += 1
    return [score_to_rank(prize_count + zero_count), 
            score_to_rank(prize_count)]

def solution(lottos, win_nums):
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
# https://programmers.co.kr/learn/courses/30/lessons/1845
# 폰켓몬.py

def solution(nums):
    set_nums = list(set(nums))
    if len(set_nums) <= len(nums)//2 :
        return len(set_nums)
    else :
        return len(nums)//2
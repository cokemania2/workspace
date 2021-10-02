# https://programmers.co.kr/learn/courses/30/lessons/82612
# 부족한 금액 계산하기.py

def solution(price, money, count):
    sum_price = 0
    for i in range(1, count+1) :
        sum_price += price * i
    return sum_price - money if sum_price > money else 0
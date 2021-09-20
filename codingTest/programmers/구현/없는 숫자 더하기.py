# https://programmers.co.kr/learn/courses/30/lessons/86051
# 없는 숫자 더하기.py

# set - set으로 차집합을 구할 수 있다.

def solution(numbers):    
    return(sum(list(set([0,1,2,3,4,5,6,7,8,9]) - set(numbers))))
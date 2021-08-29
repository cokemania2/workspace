# https://programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase 문자열 만들기.py

def solution(s):
    answer = []
    s = s.split(' ')
    for i in s:
        answer.append(i.capitalize())
    return " ".join(answer)
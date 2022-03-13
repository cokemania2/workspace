# https://programmers.co.kr/learn/courses/30/lessons/12930
# 이상한문자 만들기.py

def solution(s):
    answer = []
    s = list(s.split(' '))
    for a in s :
        tmp = []
        for i in range(len(a)) :
            if (i % 2 == 0) :
                tmp.append(a[i].upper())
            else :
                tmp.append(a[i].lower())
        answer.append("".join(tmp))
    return " ".join(answer)
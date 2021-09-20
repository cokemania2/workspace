# https://programmers.co.kr/learn/courses/30/lessons/84325
# 직업군 추천하기.py


def solution(table, languages, preference):
    answer = ''    
    count = []
    for i in table:
        i = i.split()
        score = 0
        for j in range(1, len(i)):
            for z in range(len(languages)):
                if i[j] == languages[z]:
                    score += preference[z] * (5 - j + 1)
        count.append(score)
    maxv = 0
    maxi = 0
    for i in range(len(count)):
        if count[i] > maxv:
            maxv = count[i]
            maxi = i
        if count[i] == maxv and table[i].split()[0] < table[maxi].split()[0]:
            maxv = count[i]
            maxi = i
    return table[maxi].split()[0]
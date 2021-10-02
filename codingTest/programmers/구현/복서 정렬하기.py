# https://programmers.co.kr/learn/courses/30/lessons/85002
# 복서 정렬하기.py

def solution(weights, head2head):
    result = []
    
    for i,record in enumerate(head2head):
        h = []
        w = 0
        c = 0
        t = 0
        for j,v in enumerate(record):
            if v == 'N':
                continue
            if v == 'W':
                w += 1
                if weights[i] < weights[j]:
                    c += 1
            t += 1
        result.append([w/t * 100 if w != 0 else 0, c, weights[i], i+1])
    result = sorted(result,key=lambda x : (-x[0],-x[1],-x[2],x[3]))
    return [i[3] for i in result]
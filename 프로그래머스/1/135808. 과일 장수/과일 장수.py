def solution(k, m, score):
    summ = 0 
    score = sorted(score, reverse=True)
    for i in range(0, len(score), m):
        box = score[i:i+m]
        if len(box) == m:
            summ += min(box) * m
    return summ
            
        
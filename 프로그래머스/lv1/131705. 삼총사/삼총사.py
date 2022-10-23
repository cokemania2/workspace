from itertools import combinations
    

def solution(number):
    answer = 0
    for v_set in list(combinations(number, 3)):
        if sum(v_set) == 0:
            answer += 1
    return answer

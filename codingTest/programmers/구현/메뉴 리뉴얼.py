from itertools import combinations

def solution(orders, course):
    answer = []
    dic = {}
    max_set = {}
    for i in course:
        max_set[i] = [[],0]
    
    # 조합별로 나온 횟수 저장
    for order in orders:
        for c in course:
            for a in list(combinations(order, c)):
                a = ''.join(list(sorted(list(set(a)))))
                if a in dic:
                    dic[a] += 1
                else:
                    dic[a] = 1
    # 코스별 최대 횟수 저장
    for k, v in dic.items():
        if v > max_set[len(k)][1]:
            max_set[len(k)] = [[''.join(list(k))], v]
        elif v == max_set[len(k)][1]:
            max_set[len(k)][0].append(''.join(list(k)))
    
    # 2번 이상 나온 코스 저장
    for k, v in max_set.items():
        if v[1] > 1:
            answer += v[0]
    return list(sorted(answer))
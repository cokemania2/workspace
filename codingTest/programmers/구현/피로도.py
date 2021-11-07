# https://programmers.co.kr/learn/courses/30/lessons/87946
# 피로도.py


import copy

def fun(dungeons, i, k):
    result_list = []
    if len(dungeons) == 0:
        return 0
    else:
        if k < dungeons[i][0]:
            return len(dungeons)
        else:
            k -= dungeons[i][1]
            dungeons = copy.deepcopy(dungeons[:i] + dungeons[i+1:])
            for i in range(len(dungeons)):
                result_list.append(fun(dungeons, i, k))
            if len(result_list) == 0:
                return 0
            else:
                return min(result_list)
        

def solution(k, dungeons):
    max = 0
    
    for i in range(len(dungeons)):
        result = len(dungeons) - fun(dungeons, i,  k)
        if result > max:
            max = result 
    
    return max
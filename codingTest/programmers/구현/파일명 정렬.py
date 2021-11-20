# https://programmers.co.kr/learn/courses/30/lessons/17686
# 파일명 정렬.py

import re
from functools import cmp_to_key

def compare(i1,i2):
    name1 = re.split('(\d+)', i1)
    name2 = re.split('(\d+)', i2)
    name1[0] = name1[0].upper()
    name2[0] = name2[0].upper()
    name1[1] = int(name1[1])
    name2[1] = int(name2[1])
    
    if name1[0] < name2[0]:
        return -1
    elif name1[0] == name2[0]:
        if name1[1] < name2[1]:
            return -1
        else:
            return 1
    else:
        return 1
def solution(files):
    result = sorted(files,key=cmp_to_key(compare))
    return result
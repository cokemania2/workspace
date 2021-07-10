from functools import cmp_to_key

def compare(x,y) :
    if int(str(x)+str(y)) > int(str(y)+str(x)) :
        return -1
    else :
        return 1

def solution(numbers):
    answer = "".join(map(str,sorted(numbers,key=cmp_to_key(compare))))
    return answer

print(solution([3, 30, 34, 5, 9]))

def solution(n,a,b):
    answer = 1
    if (a > b) :
        tmp = b
        b = a
        a = tmp
    while (True) :
        if b % 2 == 0 :
            if b - a == 1 :
                return answer
        if a % 2 == 0 :
            a //= 2
        else :
            a = a // 2 + 1
        if b % 2 == 0 :
            b //= 2
        else :
            b = b // 2 + 1
        answer += 1
    return answer

print(solution(8,4,7))

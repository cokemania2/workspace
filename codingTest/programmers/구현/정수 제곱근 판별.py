def solution(n):
    if n == 1 :
        return 4
    for i in range(n // 2) :
        if n == i * i :
            return (i+1) * (i+1)
        if i * i > n :
            break
    return -1
# https://www.acmicpc.net/submit/2231/33993821
# 분해합.py

def int_if_digit(n):
    if n.isdigit():
        return int(n)
    return 0

def solution(N, maxV):
    for i in range(int(N)-maxV,int(N)):
        if i + sum(list(map(int_if_digit ,list(str(i))))) == int(N):
            return i
    return 0

N = input()
maxV = len(N) * 9
print(solution(N, maxV))
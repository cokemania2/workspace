# https://www.acmicpc.net/problem/11816
# 8진수, 10진수, 16진수.py

def rule(n, x):
    answer = 0
    dic = {}
    for i in range(10) :
        dic[str(i)] = i
    if n == 16:
        for i in range(7):
            dic[chr(ord('a')+i)] = 10+i
    for i,v in enumerate(list(reversed(x))):
        answer += dic[v]*(n**i)
    return answer

def solution(x):
    if len(X) == 1:
        return int(X)    
    if "".join(x[:2]) == '0x':
        return rule(16, x[2:])
    elif x[0] == '0':
        return rule(8, x[1:])
    else :
        return int("".join(x))
X = list(input())
print(solution(X))
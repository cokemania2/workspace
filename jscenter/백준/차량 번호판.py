##https://www.acmicpc.net/problem/16968
##차량 번호판

answer = 1
tmp = 'N'
s = list(input())
for i in s :
    d = 10
    c = 26
    if tmp == i :
        d -= 1
        c -= 1
    if i == 'd' :
        answer *= d
        tmp = 'd'
    elif i == 'c' :
        answer *= c
        tmp = 'c'
print(answer)
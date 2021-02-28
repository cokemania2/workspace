# https://www.acmicpc.net/problem/1292
# 쉽게 푸는 문제.py

# 쉬운문제인데 .. 꽤걸림

a, b = map(int,input().split(' '))
answer = 0
level = 1
n = 0
for i in range (b) :
    if n < level :
        if i >= a - 1 :
            answer += level
        n += 1
    if n == level :
        n = 0
        level += 1
print(answer)

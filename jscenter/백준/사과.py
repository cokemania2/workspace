# https://www.acmicpc.net/problem/10833
# 사과

answer = 0
N = int(input())
for i in range(N) :
    a, b = map(int,input().split(' '))
    b -=  a * (b // a)
    answer += b
print(answer)

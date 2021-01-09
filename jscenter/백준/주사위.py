# https://www.acmicpc.net/problem/9295

T = int(input())
for i in range(T) :
    a, b = map(int,input().split(' '))
    print('Case',i+1,end='')
    print(':',a+b)
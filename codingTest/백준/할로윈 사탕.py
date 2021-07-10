https://www.acmicpc.net/problem/10178

T = int(input())
for i in range(T) :
    c, v = map(int,input().split(' '))
    print('You get',c // v,'piece(s) and your dad gets',c % v,'piece(s).')
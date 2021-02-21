##https://www.acmicpc.net/problem/10214
##Baseball

T = int(input())

for i in range(T) :
    y = 0
    k = 0
    for j in range(9) :
        a, b = map(int, input().split(' '))
        y += a
        k += b
    if y > k :
        print('Yonsei')
    else :
        print('Korea')
##https://www.acmicpc.net/problem/17010
##Time to Decompress

L = int(input())
for i in range(L) :
    N, x = input().split(' ')
    for i in range(int(N)) :
        print(x, end='')
    print()
##https://www.acmicpc.net/problem/11653
##소인수 분해

# 작은수 부터 차례대로 나눠주면 소인수 분해가 잘 된다.

N = int(input())
while N > 1 :
    for i in range (2,N + 1) :
        if N % i == 0 :
            N //= i
            print(i)
            break
# https://www.acmicpc.net/problem/1755
# 숫자놀이.py

def change_int(n):
    number = ['zero','one','two','three','four','five','six','seven','eight','nine']
    a = ''
    if n // 10 > 0:
        a = number[n // 10]
    b = number[n % 10]
    return a + b


M, N = map(int,input().split())
num = list(sorted([i for i in range(M, N+1)],key=lambda x : change_int(x)))
for i, v in enumerate(num):
    if i != 0 and i % 10 == 0:
        print()
    print(v,end=' ')
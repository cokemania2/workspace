# https://www.acmicpc.net/problem/1735
# 분수 합.py

def uclid(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a 

a, A = map(int, input().split())
b, B = map(int, input().split())
gcd = uclid(a*B+b*A, A*B)
print((a*B+b*A)//gcd, A*B//gcd)
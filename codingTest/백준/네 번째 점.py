# https://www.acmicpc.net/problem/3009
# 네 번째 점.py

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
print(a[0] ^ b[0] ^ c[0], a[1] ^ b[1] ^ c[1])
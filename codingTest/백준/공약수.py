# 공약수.py
# https://www.acmicpc.net/problem/5618

import math
k = int(input())
n_list = list(map(int,input().split()))
answer = []
if k == 2:
    maxV =  math.gcd(n_list[0], n_list[1])
else :
    maxV = math.gcd(math.gcd(n_list[0], n_list[1]), n_list[2])
for i in range(1, int(maxV**0.5)+1):
    if maxV % i == 0:
        answer+=[i, maxV//i]
for i in sorted(set(answer)) :
    print(i)
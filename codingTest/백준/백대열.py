# https://www.acmicpc.net/problem/14490
# 백대열.py

import math

a, b = map(int,input().split(':'))
n = math.gcd(a,b)
print(str(a//n)+":"+str(b//n))
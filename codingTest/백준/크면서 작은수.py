# https://www.acmicpc.net/problem/2992
# 크면서 작은수.py
import itertools

def join_and_int(x):
    return int("".join(x))

x = list(input())
nPr = itertools.permutations(x)
try:
    a = list(sorted(set(list(map(join_and_int,nPr)))))
    index = a.index(join_and_int(x))
    print(a[index+1])
except:
    print(0)
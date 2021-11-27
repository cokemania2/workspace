# https://www.acmicpc.net/problem/1302
# 베스트셀러.py

from functools import cmp_to_key

def compare(x,y):
    if x[1] == y[1]:
        if x[0] < y[0] :
            return -1
        else:
            return 1
    
    elif x[1] < y[1]:
        return 1
    else:
        return -1

N = int(input())
book = {}
for i in range(N):
    name = input()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1
result = sorted(book.items(), key=cmp_to_key(compare))
print(result[0][0])

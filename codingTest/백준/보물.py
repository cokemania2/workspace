# https://www.acmicpc.net/submit/1026/36529125
# 보물.py

N = int(input())
a = list(sorted(list(map(int, input().split()))))
b = list(sorted(list(map(int, input().split())), reverse=True))
c = [a[i] * b[i] for i in range(len(a))]
print(sum(c))

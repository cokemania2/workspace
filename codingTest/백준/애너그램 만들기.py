# 애너그램 만들기.py
# https://www.acmicpc.net/problem/1919

# good code 
a = input()
b = input()

print(sum([abs(a.count(i) - b.count(i)) for i in set(a+b)]))

# bad code
from collections import Counter

answer = 0
a = input()
b = input()
a = Counter(a)
b = Counter(b)
for i in a:
    if i in b:
        answer += abs(a[i] - b[i])
    else:
        answer += a[i]
for i in b:
    if i not in a:
        answer += b[i]
print(answer)
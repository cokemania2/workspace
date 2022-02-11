# https://www.acmicpc.net/problem/5555
# 반지.py

find_word = input()
n = int(input())
count = 0
for i in range(n):
    ring = input()
    if (ring+ring).find(find_word) != -1:
        count += 1
print(count) 
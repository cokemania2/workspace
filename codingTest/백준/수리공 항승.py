# https://www.acmicpc.net/problem/1449
# 수리공 항승.py

N, L = map(int, input().split())
whole = list(sorted(list(map(int, input().split()))))

count = 0
covered = -1
for i in whole:
    if i > covered:
        covered = i + L - 1
        count += 1
print(count)
# https://www.acmicpc.net/problem/14582
# 오늘도 졌다.py

j = list(map(int, input().split()))
s = list(map(int, input().split()))
j_sum, s_sum = 0, 0
flag = False
for i in range(9):
    j_sum += j[i]
    if j_sum > s_sum:
        flag = True
    s_sum += s[i]
if j_sum < s_sum and flag:
    print('Yes')
else:
    print('No')    
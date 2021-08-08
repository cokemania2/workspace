# https://www.acmicpc.net/submit/1978/31827170
# 소수 찾기.py

s = [0]*1001
s[1] = 1
for i in range(2, 1000) :
    for j in range(2, 1000) :
        if i * j > 1000 :
            break
        if s[i * j] == 0 :
            s[i * j] = 1


N = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if s[i] == 0:
        count += 1
print(count)
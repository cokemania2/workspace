# https://www.acmicpc.net/problem/3059
# 등장하지 않는 문자의 합.py

T = int(input())
for i in range(T):
    arr = []
    for i in range(ord('Z')-ord('A')+1):
        arr.append(65+i)

    S = list(input())
    for i in S :
        arr[ord(i)-65] = 0
    print(sum(arr))
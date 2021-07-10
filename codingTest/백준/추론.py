# https://www.acmicpc.net/problem/1731
# 어려운 문제가 아닌데 오래걸렸다.
# 앞의 세자리만 비교해도 등차인지 등비인지 비교해서 계산.


arr = []
N = int(input())
for i in range (N) :
    arr.append(int(input()))
if arr[-1] - arr[-2] == arr[-2] - arr[-3] :
    print(int(arr[-1] + (arr[2] - arr[1])))
else :
    print(int(arr[-1] * (arr[2] / arr[1])))

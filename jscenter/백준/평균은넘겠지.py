# https://www.acmicpc.net/problem/4344
# 소수점을 신경써야 하는 부분이 어렵다.

C = int(input())
for i in range(C) :
    arr = list(map(int,input().split()))
    avr = sum(arr[1:]) / arr[0]
    arr2 = [i for i in arr[1:] if i > avr]
    result = round((len(arr2)/(len(arr)-1)),6) * 100 
    print('{:.3f}%'.format(result))
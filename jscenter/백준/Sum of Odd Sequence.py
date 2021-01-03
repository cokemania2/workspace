# https://www.acmicpc.net/problem/9713
# Sum of Odd Sequence

dic = {}
dic[1] = 1
T = int(input())
for i in range(3,100) :
    if i%2 == 1 :
        dic[i] = dic[i-2] + i
for i in range(T) :
    N = int(input())
    print(dic[N])
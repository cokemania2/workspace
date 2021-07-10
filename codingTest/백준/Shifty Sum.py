##https://www.acmicpc.net/problem/14682
##Shifty Sum

n = int(input())
k = int(input())
answer = n
for i in range(k) :
    n *= 10
    answer += n
print(answer)
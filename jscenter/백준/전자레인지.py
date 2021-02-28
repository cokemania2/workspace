##https://www.acmicpc.net/problem/10162
##전자레인지

ABC = [300, 60, 10]
answer = []
T = int(input())
for i in ABC :
    c = T // i
    T -= i * c
    answer.append(c)
if T != 0 :
    print(-1)
else :
    for i in answer :
        print(i,end=' ')
M = int(input())
N = int(input())
arr = [False, False] + [True]*(N+1)
answer = []
for i in range(2,N+1) :
    for j in range(2,N) :
        if i*j > N:
            break
        if arr[i*j]:
            arr[i*j] = False
for i in range(M,N+1) :
    if arr[i] :
        answer.append(i)
if len(answer) == 0 :
    print(-1)
else :
    answer = sorted(answer)
    print(sum(answer))
    print(answer[0])
A = int(input())
B = int(input())
C = int(input())

N = str(A * B * C)
for i in range(0,10) :
    cnt = 0
    for j in range(len(N)) :
        if int(N[j]) == i :
            cnt += 1
    print(cnt)


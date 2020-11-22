A = int(input())
B = int(input())
C = int(input())

N = str(A * B * C)
for i in (1,10) :
	cnt = 0
	for j in len(N) :
		if int(N[j]) == i :
			cnt++
	print(cnt)
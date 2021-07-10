# 100 이전 한자릿수나 두 자릿수는 등차수열이므로 바로 출력해준다.
# 100 이상부터는 비교를 해주며 N을 ++해 주었다.

N = 99
a = int(input())
if a < 100 :
	print(a)
else :
	while a > 100 :
		b = list(map(int,list(str(a))))
		if ((b[0] - b[1]) == (b[1] - b[2])) :
			N += 1
		a -= 1
	print(N)
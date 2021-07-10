#모든 경우의 수를 넣어보는 brute-force 방법을 이용했다.
#파이썬의 순열(permutations)을 이용했다.

import itertools

maxx = 0
N = int(input())
pool = list(itertools.permutations(list(input().split())))
for p in pool :
	p = list(map(int,list(p)))
	summ = 0
	for i in range(1,len(p)) :
		summ += abs(p[i - 1] - p[i])
	if summ > maxx :
		maxx = summ
print(maxx)
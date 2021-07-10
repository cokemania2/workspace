##https://www.acmicpc.net/problem/2966

Adrian = ['A', 'B', 'C']
Bruno = ['B', 'A', 'B', 'C']
Goran = ['C', 'C', 'A', 'A', 'B', 'B']
A = 0
B = 0
C = 0

N = int(input())
test = list(input())
for i in range (N) :
    if test[i] == Adrian[i % 3] :
        A += 1
    if test[i] == Bruno[i % 4] :
        B += 1
    if test[i] == Goran[i % 6] :
        C += 1
print(max(max(A,B),C))
if A >= B and A >= C :
    print('Adrian')
if B >= A and B >= C :
    print('Bruno')
if C >= B and C >= A :
    print('Goran')

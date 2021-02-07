n, T = map(int,input().split(' '))
FCFS = list(map(int,input().split(' ')))
summ = 0
flag = True
for i in range (n) :
    summ += FCFS[i]
    if summ > T :
        print(i)
        flag = False
        break
if flag == True :
    print(n)

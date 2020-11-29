summ = 0
Rsum = 0
N = int(input())
time = sorted(list(map(int,input().split(' '))))
for i in time :
    summ += i
    Rsum += summ
print(Rsum)
    

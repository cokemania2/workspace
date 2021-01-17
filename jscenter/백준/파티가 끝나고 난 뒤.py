L , P = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))
area = L * P
for i in range (5) :
    print(arr[i] - area,end = ' ')

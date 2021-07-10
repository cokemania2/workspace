arr = []
N = int(input())
for i in range(N) :
    arr.append(input().split(' '))
arr = sorted(arr, key = lambda x : int(x[0]))
for i in arr :
    print(i[0],i[1])
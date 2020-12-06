arr = []

for i in range(8) :
    arr.append(int(input()))
for i in range(3) :
    arr[arr.index(min(arr))] = 151
print(sum(arr) - 151 * 3)
for i in range(8) :
    if arr[i] != 151 :
        print(i + 1,end = ' ')

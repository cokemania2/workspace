while True :
    summ = 0
    arr = list(map(int,input().split(' ')))
    if arr[0] == -1 :
        break
    for i in arr :
        if i == 0 :
            break
        summ +=  arr.count(i * 2)
    print(summ)

while (True) :
    arr = input().split(' ')
    if arr[0] == '#' :
        break
    print(arr[0],end=' ')
    if int(arr[1]) > 17 or int(arr[2]) >= 80 :
        print('Senior')
    else :
        print('Junior')
        

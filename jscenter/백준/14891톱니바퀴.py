def rot(arr, n, c) :
    if (c == 1) :
        tmp = arr[n].pop()
        arr[n].insert(0,tmp)
    else :
        tmp = arr[n].pop(0)
        arr[n].append(tmp)
        
def top(n, c, arr, arr2) :
    if (arr2[n] == 0) :
        arr2[n] = 1
        if (n == 0) :
            if (arr[n][2] != arr[n + 1][6]) :          
                top(n + 1, -c, arr, arr2)
        elif (n == 1 or n == 2) :
            if (arr[n][2] != arr[n + 1][6]) : # 오른쪽
                top(n + 1, -c, arr, arr2)
            if (arr[n][6] != arr[n - 1][2]) : # 왼쪽
                top(n - 1, -c, arr, arr2)
        else :
            if (arr[n][6] != arr[n - 1][2]) :
                top(n - 1, -c, arr, arr2)
        rot(arr, n, c)
		
if __name__ == '__main__' :

    arr = [[0] * 8] * 4
    summ = 0
    point = 1

    for i in range (4) :
        arr[i] = list((input()))
    K = int(input())
    for i in range (K) :
        arr2 = [0] * 4
        n, c = map(int,(input().split()))
        n = n - 1
        top(n, c, arr, arr2)
    for i in range (4) :
        if (arr[i][0] == '1') :
            summ += point
        point = point * 2
    print(summ)

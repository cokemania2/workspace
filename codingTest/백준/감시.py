def fun2(N, M, Z, arr) :
    if (Z == 1) :
        for i in range (N) :
            
    elif (Z == 2) :
    elif (Z == 3) :
    elif (Z == 4) :
    elif (Z == 5) :

def fun(N, M, arr) :
    for i in range (N) :
        for j in range (M) :
            if (arr[i][j] >= 1 and arr[i][j] <= 5) :
                fun2(i, j, arr[i][j], arr)
                
            
        
if __name__ == '__main__' :
    N, M = map(int,input().split())
    maxv = 0
    arr = [[0] * M] * N
    for i in range(N) :
        arr[i] = (int)input().split(' ')
    fun(0, 0, arr)
    

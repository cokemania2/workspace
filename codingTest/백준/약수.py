n = int(input())
for i in range (n) :
    arr = list(map(int,input().split()))
    a =((arr[3]-arr[0])**2+(arr[4]-arr[1])**2)**0.5 
    if ( arr[0] == arr[3] and arr[1] == arr[4]) : #좌표가 같고
        if (arr[2] == arr[5]) : # 완벽하게 같음 
            print('-1')
        else :  # 원안에 원 형태 
            print('0')
    elif ( a == arr[5]+arr[2] or a== abs(arr[5]-arr[2])) :
        print('1')
    elif ( a < arr[5]+arr[2] ) :
        print('2')
    elif ( a > arr[5]+arr[2] ) :
        print('0')

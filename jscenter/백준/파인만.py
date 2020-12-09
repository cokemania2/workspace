def fun(N) :
    if N == 1 :
        return 1
    return (N * N) + fun(N - 1)

while True :
    N = int(input())
    if N == 0 :
        break
    print(fun(N))
        

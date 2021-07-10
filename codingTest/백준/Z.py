# https://www.acmicpc.net/source/17614382
# 마지막에 크기가 1이 될때까지 
# 1,2,3,4 분면으로 나눠서 덩어리를 계속 쪼개준다.
# 덩어리가 시작되는 크기만큼 answer에 더해준다.

N, r, c = map(int,input().split(' '))
answer = 0
N = (2 ** N)
cal = N * N
while True :
    if r < N / 2 :
        if c >= N / 2 :
            answer += cal / 4 # 1사분면
            c -= N / 2
    else :
        r -= N / 2
        if c < N / 2 :
            answer += cal / 2 # 3사분면
        else : 
            answer += (cal / 4) * 3 # 4사분면
            c -= N / 2
    if N / 2 == 1 :
        print(int(answer))
        break
    else :
        cal /= 4
        N /= 2

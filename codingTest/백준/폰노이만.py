P = int(input())
for i in range(P) :
    NDABF = list(map(float,input().split()))
    print(int(NDABF[0]),end = ' ')
    print('%0.6f' %  float((NDABF[1] / (NDABF[2] + NDABF[3]) * NDABF[4])))
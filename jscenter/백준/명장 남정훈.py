##https://www.acmicpc.net/problem/15734
##명장 남정훈

# 큰수를 R로 옮기고 한번만 판단했다.
# 왼발, 오른발 차이가 A 보다 클 경우 작은 수에 A를 더하고 작은 수 * 2하면 되고
# 차이가 더 적을경우 먼저 차이를 없게 만들고, A를 분배 ( 나누기 2로 균등하게)
# 해주고 * 2 해주면 된다 (균등하기 때문에)

l, r , A = map(int,input().split(' '))
R = max(l, r)
L = min(l, r)
if R - L > A :
    print((L + A) * 2)
else :
    A -= R - L
    print((R + A // 2)* 2)

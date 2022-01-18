# https://www.acmicpc.net/problem/4796
# 캠핑.py

# 앞에서 L일동안 텐트를 사용하고 L일 포함 P일이 지난 후 다시 텐트를 사용하는 식으로 사용해야 최대한 많이 쓸 수 있다.
# (V // P) V이를 연속되는 P일로 나눈 후 * 텐트를 칠 수 있는 L일을 곱한다. -> 규칙적으로 쓸 수 있는 날 
# min(L, V % P)) -> 남은 날은 나머지 날과 텐트를 칠 수 있는 L보다 크면 안되기때문에 min으로 계산해준다. 

case = 1
while True:
    # L = 텐트 사용 가능 , P = 캠핑장에 연속해서 머무는 날 , V = 휴가일수 
    L, P , V = map(int, input().split())
    if L+P+V == 0:
        break
    print("Case "+str(case)+": "+str((V // P) * L + min(L, V % P)))
    case += 1
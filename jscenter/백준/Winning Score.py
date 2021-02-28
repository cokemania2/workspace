# https://www.acmicpc.net/problem/17009
# Winning Score

# AppleTeam vs BananaTeam
# 위 세개의 수는 애플팀 밑 세개의 수는 바나나팀
# 세 숫자는 차례대로 3점슛, 2점슛, 1점슛
# 점수 비교

AppleTeam = 0
BananaTeam = 0
A = 3
B = 3
for i in range(6) :
    if i < 3 :
        AppleTeam += int(input()) * A
        A -= 1
    else :
        BananaTeam += int(input()) * B
        B -= 1
if AppleTeam > BananaTeam :
    print('A')
elif BananaTeam > AppleTeam :
    print('B')
else :
    print('T')

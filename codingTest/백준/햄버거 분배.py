# https://www.acmicpc.net/problem/19941
# 햄버거 분배.py

N, K = map(int, input().split())
HP = list(input())
print(HP)
for i, v in enumerate(HP):
    if v == 'P':
        for j in range(K,0,-1):
            if i-j >= 0 and HP[i-j] == 'H':
                HP[i-j] = '🦴'
                HP[i] = '😋'
                break
            elif i+K-j < len(HP) and HP[i+K-j] == 'H':
                HP[i+K-j] = '🦴'
                HP[i] = '😋'
                break
print(HP)
print(HP.count('😋'))


# https://www.acmicpc.net/problem/1339
# 단어 수학.py

dic = dict()
answer_dic = dict()
board = []
for i in range(26):
    dic[chr(ord('A')+i)] = 0
    
N = int(input())
for i in range(N):
    x = input()[::-1]
    board.append(x)
    for j in range(len(x)):
        dic[x[j]] += 1 * (10 ** j)
res = sorted(dic.items(), key=lambda x : x[1],reverse=True)
start_n = 9
for i in res:
    if i[1] == 0:
        break
    answer_dic[i[0]] = start_n
    start_n -= 1

answer = 0
for s in board:
    for i, v in enumerate(s):
        answer += answer_dic[v] * (10 ** i)
        
print(answer)
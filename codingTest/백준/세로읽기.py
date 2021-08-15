https://www.acmicpc.net/problem/10798
세로읽기.py

answer = ""
maxLen = 0
arr = []
for i in range(5):
    tmp = input()
    arr.append(tmp)
    if  len(tmp) > maxLen:
        maxLen = len(tmp)

for i in range(maxLen):
    for j in range(5):
        if len(arr[j]) > i and arr[j][i]:
            answer += arr[j][i]
    
print(answer)
# 명령 프롬프트.py
# https://www.acmicpc.net/problem/1032

def findPattern(first, n,  arr):
    answer = ''
    for i in range(len(first)):
        flag = False
        for j in range(n-1):
            if arr[j][i] != first[i]:
                answer += '?'
                flag = True
                break
        if not flag:
            answer += first[i]
    return answer
        
arr = []
n = int(input())
first = input()
for i in range(1, n):
    arr.append(input())
print(findPattern(first, n, arr))
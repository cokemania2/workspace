# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
# 체육복.py

# 여벌의 체육복을 가지고 있는 학생들을 기준으로 앞, 그리고 뒤의 순서 대로 체육복을 준다.
# 자신의 여분 체육복을 도난당한 경우 여별의 체육복이 있음에도 옆사람이 먼저 빌려줄 수 있으므로
# 자신의 체육복을 먼저 챙기는 for문을 돌려준다.

def solution(n, lost, reserve):
    arr = [1] * n
    newReserve = []
    for i in lost :
        arr[i - 1] = 0
    for i in reserve :
        if i in lost :
            arr[i - 1] = 1
        else :
            newReserve.append(i)
    for i in newReserve :
        i = i - 1
        if arr[i] == 0 :
            arr[i] = 1
        elif i - 1 >= 0 and arr[i-1] == 0 :
            arr[i-1] = 1
        elif i + 1 < n and arr[i+1] == 0 :
            arr[i+1] = 1
    return sum(arr)
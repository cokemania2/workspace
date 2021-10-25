# https://programmers.co.kr/learn/courses/30/lessons/12949
# 행렬의 곱셈.py

# 행렬의 곱셉은 첫번째 행렬의 행과 두번째 행렬의 열을 곱해서 값을 구한다.

def solution(arr1, arr2):
    answer = []
    # 첫번째 행렬의 행 
    for i,v in enumerate(arr1):
        result = []
        # 두번째 행렬의 열만큼 반복
        for j in range(len(arr2[0])):
            result2 = 0
            for k in range(len(v)):
                result2 += arr1[i][k] * arr2[k][j]
            result.append(result2)
        answer.append(result)
    return answer
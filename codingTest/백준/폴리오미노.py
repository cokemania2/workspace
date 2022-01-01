# https://www.acmicpc.net/problem/1343
# 폴리오미노.py

def X_to_AB(count):
    answer = ""
    answer += "AAAA" * (count // 4)
    answer += "BB" if count % 4 == 2 else ""
    return answer

def polyomino(s):

    answer = ""
    count = 0
    for i in s:
        if i == 'X':
            count += 1
        else:
            if count % 2 != 0:
                return "-1"
            answer += X_to_AB(count)
            answer += "."
            count = 0
    if count % 2 != 0:
        return "-1"
    answer += X_to_AB(count)
    return answer
    
print(polyomino(input()))

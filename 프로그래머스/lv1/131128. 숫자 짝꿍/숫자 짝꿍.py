from collections import Counter

def solution(X, Y):
    answer = ''.join(sorted((Counter(X) & Counter(Y)).elements(), reverse=True))
    if answer == '':
        return "-1"
    if answer[0] == '0':
        return "0"
    return answer
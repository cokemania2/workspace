from collections import Counter

def solution(X, Y):
    answer = ''.join(sorted((Counter(X) & Counter(Y)).elements(), reverse=True))
    if answer == '':
        return "-1"
    # return str(int(asnwer)) 방법은 시간초과가 걸림
    if answer[0] == '0':
        return "0"
    return answer
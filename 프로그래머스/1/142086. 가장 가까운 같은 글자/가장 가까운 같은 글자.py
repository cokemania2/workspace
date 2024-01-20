def solution(s):
    answer = []
    str_dict = {}
    for i, v in enumerate(s):
        if v in str_dict:
            answer.append(i - str_dict[v])
        else:
            answer.append(-1)
        str_dict[v] = i 
    return answer
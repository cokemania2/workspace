def solution(gems):
    dic = {}
    answer = []
    minn = len(gems)
    arr = set(gems)
    length = len(arr)
    for i, x in enumerate(gems) :
        dic[x] = i + 1
        listdic = list(dic.values())
        if (len(listdic) == length) :
            minimum = min(listdic)
            if (i + 1 - minimum == length -1 ) :
                return [minimum, i + 1]
            elif (minn > i + 1 - minimum) :
                minn = i + 1 - minimum
                answer = [minimum, i + 1]

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

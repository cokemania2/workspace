def solution(participant,completion):
    a = {}
    for i in range (len(participant)) :
        if ( participant[i] in a ) :
            a[participant[i]] = a[participant[i]] + 1
        else :
            a[participant[i]] = 1

    for i in range (len(completion)) :
        if (completion[i] in a ) :
            a[completion[i]] = a[completion[i]] - 1
        if a[completion[i]] == 0 :
            del a[completion[i]]
    return (list(a.keys())[0])
print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))


def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    for c in completion:
        if c in dic:
            dic[c] -= 1
            if dic[c] == 0:
                del dic[c]
    for key in dic:
        return key
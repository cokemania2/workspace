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

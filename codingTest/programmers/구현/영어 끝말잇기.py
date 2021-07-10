def solution(n, words):
    answer = []
    dic = {}
    before = ''
    for i in range(len(words)) :
        if words[i] in dic :
            return [i%n +1,i//n +1]
        else :
            if before == '' or before == words[i][0] :
                dic[words[i]] = 1
            else :
                return [i%n +1,i//n+1]
        before = words[i][-1]
    return [0,0]
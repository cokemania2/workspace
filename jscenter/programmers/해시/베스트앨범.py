def solution(genres, plays):
    answer = []
    a = list(set(genres))
    b = [i for i in range(0,len(plays))]
    hey = list(zip(genres,plays,b))
    hey = sorted(hey,key = lambda x : [x[0],-x[1]])
        
    c = {}
    for i in range(len(plays)) :
        if ( genres[i] in c )  :
            c[genres[i]] = c.get(genres[i]) + plays[i]
        else :
            c[genres[i]] = plays[i]
    d = (list(sorted(c.items(),key = lambda x : -x[1])))

    for i in range (len(d)) :
        cnt = 0
        for j in range (len(hey)) :
            if (d[i][0]  == hey[j][0]) :
                answer.append(hey[j][2])
                cnt = cnt + 1
            if (cnt == 2) :
                break
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
                 

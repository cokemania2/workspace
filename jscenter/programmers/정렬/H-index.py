def solution(citations):
    citations.sort()
    h = min(citations[len(citations)-1],len(citations))
    while(True) :
        tmp = list(filter(lambda x : x >= h,citations)) 
        print(h,tmp)
        if (len(tmp) >= h) :
            return h
        else :
            h = h-1
print(solution([3, 0, 6, 1, 5]))

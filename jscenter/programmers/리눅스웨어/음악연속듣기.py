def solution(play_list, listen_time):
    answer = 0
    idx = 0
    maxx = 0
    length = len(play_list)
    play_list2 = play_list + play_list
    print(play_list)
    for i in range (length - 2, 0, -1) :
        for idx in range (length) :
            summ = sum(play_list2[idx:idx + i])
            if (listen_time - summ >= 2) :
                return i + 2
    return maxx

print(solution([2, 3, 1, 4],3))
print(solution([1, 2, 3, 4],5))
print(solution([1, 2, 3, 4],20))

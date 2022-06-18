def solution(stones, k):

    min_v = min(stones)
    max_v = max(stones)
    while min_v < max_v:
        mid_v = min_v + (max_v - min_v) // 2
        count = 0
        over = False
        for i in range(len(stones)):
            if stones[i] - mid_v <= 0:
                count += 1
                if count == k:
                    over = True
                    break
            else:
                count = 0
        if over:
            max_v = mid_v - 1
        else:
            min_v = mid_v + 1
    return min_v if over else min_v + 1

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
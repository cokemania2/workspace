def get_deleted_rocks_count(rocks, distance):
    del_count = 0
    cursor = 0
    for i in range(1, len(rocks)):
        if rocks[i] - rocks[cursor] < distance:
            del_count += 1
        else:
            cursor = i
    return del_count 


def binarysearch(rocks, n):
    answer, left, right = 0, 0, rocks[-1]
    while left <= right:
        mid = (left + right) // 2
        cnt = get_deleted_rocks_count(rocks, mid)
        if cnt <= n:
            answer = max(mid, answer)
            left = mid + 1
        else:
            right = mid -1
    return answer


def solution(distance, rocks, n):    
    rocks += [0, distance]
    rocks.sort()
    return binarysearch(rocks, n)

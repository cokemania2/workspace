def is_passed(n, times, spend_time):
    for time in times:
        n -= spend_time // time
    return True if n <= 0 else False

def binary_search(times, n):
    answer = times[-1] * n
    left, right = times[0], times[-1] * n
    while left <= right:
        mid = (left + right) // 2
        if is_passed(n, times, mid):
            answer = mid if mid < answer else answer
            right = mid - 1
        else:
            left = mid + 1
    return answer

def solution(n, times):
    times.sort()
    return binary_search(times, n)

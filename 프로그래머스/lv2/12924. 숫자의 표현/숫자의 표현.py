def solution(n):
    answer = 0
    
    k = n // 2 + 1
    while k > 0:
        result = 0
        for i in range(k):
            result += k - i
            if result == n:
                answer += 1
                break
            elif result > n:
                break
        k -= 1
    
    return answer + 1 if n != n//2 + 1 else answer
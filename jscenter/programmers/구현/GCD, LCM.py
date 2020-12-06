def gcd(a, b) :
    mod = a % b
    while mod > 0 :
        a = b
        b = mod
        mod = a % b
    return b

def lcm(a, b) :
    return a * b // gcd(a, b)

def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))
    return answer
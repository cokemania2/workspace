# https://programmers.co.kr/learn/courses/30/lessons/12980?language=python3
# 점프와 순간이동.py

# 순간이동으로 이동하면 두배씩 이동한다고 생각하면 되기때문에 주어진 숫자부터 2를 나누면서
# 만약 2로 나눠지는 숫자가 아니면 1을 빼주면서 2로 나눠지게 끔 해준다.
# n을 이진수로 표현할경우 1의 갯수를 구하면 답이 나오기도 한다. (bin(n))

def solution(n):
    ans = 0
    while n != 0 :
        if n % 2 == 0 :
            n /= 2
        else :
            n -= 1
            ans += 1
    return ans
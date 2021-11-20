# https://www.acmicpc.net/problem/2744
# 대소문자 바꾸기.py

# str.swapcase()
# 파이썬 swapcase () 메소드는 대문자와 소문자의 문자열을 변환하는 데 사용됩니다.

s = input()
answer =""
for i in s:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
    answer += i
print(answer)
# https://www.acmicpc.net/problem/6749
# 삼형제의 나이차가 같을때 제일 나이많은 형의 나이를 구하는 문제

a = int(input())
b = int(input())
print(max(a,b) + abs(a-b))
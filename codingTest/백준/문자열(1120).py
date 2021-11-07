# https://www.acmicpc.net/problem/1120
# 문자열.py

def diff_w(a, b):
    answer = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            answer += 1
    return answer

a, b = input().split()
diff  = len(b) - len(a)
print(min([diff_w(a, b[i:len(a)+i])  for i in range(diff+1)]))

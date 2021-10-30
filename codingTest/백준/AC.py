# https://www.acmicpc.net/problem/5430
# AC.py

N = int(input())
for i in range(N):
    cmd = input()
    n = int(input())
    arr = input()[1:-1].split(',')
    flag = False
    R  = 1
    left = 0
    right = 0
    for w in cmd:
        if w == 'R':
            R *= -1
        else:
            if R < 0:
                right += 1
            else:
                left += 1
            if right + left > n:
                flag = True
                break
    if flag:
        print("error")
    else:
        if left != 0:
            arr[:] = arr[left:]
        if right != 0:
            arr[:] = arr[:-right]
        if R == -1:
            arr[:] = list(reversed(arr))
        print('['+",".join(arr)+']')
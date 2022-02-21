# https://www.acmicpc.net/problem/10866
# 덱.py

from collections import deque
import sys

deq = deque()
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    command = sys.stdin.readline().split()
    # push_front X: 정수 X를 덱의 앞에 넣는다.
    if command[0] == 'push_front':
        deq.appendleft(command[1])
    # push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif command[0] == 'push_back':
        deq.append(command[1])
    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.    
    elif command[0] == 'pop_front':
        print(deq.popleft() if len(deq) != 0 else -1)
    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'pop_back':
        print(deq.pop() if len(deq) != 0 else -1)
    # size: 덱에 들어있는 정수의 개수를 출력한다.
    elif command[0] == 'size':
        print(len(deq))
    # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif command[0] == 'empty':
        print(1 if len(deq) == 0 else 0)
    # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'front':
        print(deq[0] if len(deq) != 0 else -1)
    # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'back':
        print(deq[-1] if len(deq) != 0 else -1)




def solution(N, number):
    answer = [set([int('5' * i)]) for i in range(1, 9)]
    if number == N:
        return 1
    for i in range(1, 8):
        for j in range(i):
            for op1 in answer[j]:
                for op2 in answer[i-j-1]:
                    answer[i].add(op1 + op2)
                    if op1 >= op2:
                        answer[i].add(op1 - op2)
                    answer[i].add(op1 * op2)
                    if op2 != 0:
                        answer[i].add(op1 // op2)
        if number in answer[i]:
            return i + 1
    return -1
print(solution(5, 12))
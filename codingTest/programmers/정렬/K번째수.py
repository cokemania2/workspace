def solution(array, commands):
    answer = []
    for i in range(len(commands)) :
        tmp = array[commands[i][0]-1:commands[i][1]]
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])
    return answer
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

def solution(array, commands):
    answer = []
    
    for cmd in commands:
        answer.append(sorted(array[cmd[0]-1:cmd[1]])[cmd[2] - 1])
    return answer
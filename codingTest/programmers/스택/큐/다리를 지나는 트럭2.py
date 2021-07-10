def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = []
    m = []
    bridge.append(bridge_length)
    m.append(truck_weights.pop(0))
    while (len(bridge) != 0) :
        flag = False
        for i in range (len(bridge)) :
            if (bridge[i] == 1) :
                flag = True
            else :
                bridge[i] = bridge[i] - 1       
        if (flag) :
            bridge.pop(0)
            m.pop(0)
        if (len(truck_weights) != 0 and sum(m) + truck_weights[0] <= weight
            and len(bridge) <= bridge_length) :
            bridge.append(bridge_length)
            m.append(truck_weights.pop(0))
        answer = answer + 1
            
    return (answer)
	
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
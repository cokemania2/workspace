def solution(bridge_length,weight,truck_weights):
    answer = 1
    bridge = [0]*(bridge_length-1)
    bridge_weight = truck_weights.pop(0)
    bridge.append(bridge_weight)
    while ( bridge_weight != 0 ) :
        if ( len(truck_weights) != 0 and bridge_weight - bridge[0] + truck_weights[0] <= weight  ) :
            bridge_weight = bridge_weight - bridge.pop(0)
            tmp = truck_weights.pop(0)
            bridge_weight = bridge_weight + tmp
            bridge.append(tmp)
        else :
            bridge_weight = bridge_weight -bridge.pop(0)
            bridge.append(0)
        answer = answer + 1
    return answer
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))

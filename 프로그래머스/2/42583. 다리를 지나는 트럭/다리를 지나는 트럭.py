from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    waiting = deque(truck_weights)
    bridge_total_weight = 0
    answer = 0
    
    while waiting or bridge_total_weight > 0:
        answer += 1
        out = bridge.popleft()
        bridge_total_weight -= out
        
        if waiting :
            if bridge_total_weight + waiting[0] <= weight :
                truck = waiting.popleft()
                bridge.append(truck)
                bridge_total_weight += truck
            else :
                bridge.append(0)
    return answer
from collections import deque

def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    
    # 합이 홀수면 바로 불가능
    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(q1)  # queue1의 현재 합
    s2 = sum(q2)  # queue2의 현재 합
    
    max_moves = len(q1) * 3  # 최대 이동 횟수 제한
    moves = 0
    
    while moves < max_moves:
        if s1 == target:
            return moves
        
        if s1 > target:
            # queue1에서 pop
            val = q1.popleft()
            s1 -= val
            q2.append(val)
            s2 += val
        else:
            # queue2에서 pop
            val = q2.popleft()
            s2 -= val
            q1.append(val)
            s1 += val
        
        moves += 1
    
    return -1

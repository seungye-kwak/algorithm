from collections import deque

T = int(input())

def print_queue(m, lst) :
    order = []
    idx_lst = deque(list(range(0, len(lst))))
    queue = deque(lst)
    
    while queue :
        p = queue.popleft()
        idx = idx_lst.popleft()
        
        if queue and max(queue) > p :
            queue.append(p)
            idx_lst.append(idx)
        else :
            order.append(idx)
    
    answer = order.index(m) + 1
    
    return answer

for _ in range(T) :
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    
    print(print_queue(m, lst))
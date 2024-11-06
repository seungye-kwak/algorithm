from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

queue = deque([])
time = 0
for truck in trucks:
    while True:
        if sum(queue) + truck <= L and len(queue) < w:
            queue.append(truck)
            time += 1
            break
        else:
            queue.append(0)
            time += 1
            
        if len(queue) == w:
            queue.popleft()
            
    if len(queue) == w:
        queue.popleft()
print(time + w)
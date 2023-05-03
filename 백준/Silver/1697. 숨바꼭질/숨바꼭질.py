from collections import deque

start, stop = map(int, input().split())
time = [0] * 100001

def bfs(start, stop) :
    queue = deque([start])
    while queue :
        v = queue.popleft()
        if v == stop :
            return time[v]
        for i in (v-1, v+1, 2*v) :
            if 0<= i <= 100000 and not time[i] :
                time[i] = time[v] + 1
                queue.append(i)
                
print(bfs(start, stop))
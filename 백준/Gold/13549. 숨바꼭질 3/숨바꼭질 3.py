n, k = map(int, input().split())

from collections import deque

visited = [False]*100001
time = [float('inf')]*100001

def bfs(n, visited, time):
    queue = deque([n])
    visited[n] = True
    time[n] = 0
    while queue and visited[k] == False:
        x = queue.popleft()
        
        for i in [2*x, x-1, x+1]:
            if 0 <= i <= 100000 and visited[i] == False:
                visited[i] = True
                
                if i == 2*x :
                    time[i] = time[x]
                    queue.appendleft(i)
                else :
                    time[i] = time[x] + 1
                    queue.append(i)
    print(time[k])
    
bfs(n, visited, time)
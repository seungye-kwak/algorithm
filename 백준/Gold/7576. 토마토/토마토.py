from collections import deque
import sys
m, n = map(int, input().split())

storage = []
starts = []
for i in range(n) :
    lst = list(map(int, input().split()))
    for j in range(m) :
        if lst[j] == 1 :
            starts.append((i, j))
    storage.append(lst)
    
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 없는 칸
visited = [[0] * m for _ in range(n)]

def bfs(starts, visited) :
    queue = deque(starts)
    for start in starts :
        visited[start[0]][start[1]] = 1
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny <0 or ny>= m :
                continue
            
            if storage[nx][ny] == -1 :
                visited[nx][ny] = -1
                
            if storage[nx][ny] == 0 and visited[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
    return visited

visited = bfs(starts, visited)

max_time = 0
for i in range(n) :
    for j in range(m) :
        if visited[i][j] == 0 and storage[i][j] == 0 :
            print(-1)
            sys.exit(0)
        if visited[i][j] > 0 :
            max_time = max(max_time, visited[i][j]-1)
        
print(max_time)
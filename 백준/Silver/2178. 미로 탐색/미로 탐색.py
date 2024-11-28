from collections import deque

n, m = map(int, input().split())

# 미로
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = [int(x) for x in input()]
    
#방문 여부 
visited = [[0]*m for _ in range(n)]

def bfs(graph, visited):
    cnt = 0
    queue = deque([(0,0)])
    visited[0][0] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    print(visited[-1][-1])
    
bfs(graph, visited)
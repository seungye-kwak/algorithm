from collections import deque

n, m = map(int, input().split())
papers = [[int(x) for x in input().split()] for _ in range(n)]

def bfs(start, graph, visited):
    size = 1
    queue = deque([start])
    visited[start[0]][start[1]] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or nx >=n or ny <0 or ny>=m:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                size +=1
    return size

visited = [[0]*m for _ in range(n)]
cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and papers[i][j] == 1:
            cnt += 1
            max_size = max(max_size, bfs((i,j), papers, visited))
            
print(cnt)
print(max_size)
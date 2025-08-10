n, m = map(int, input().split())
maps = [[int(x) for x in input()] for _ in range(n)]

from collections import deque
def bfs(start, maps, visited) :
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or nx >= n or ny < 0 or ny >= m :
                continue
            
            if maps[nx][ny] == 1 and visited[nx][ny] == 0 :
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
    return visited[n-1][m-1]

visited = [[0] * m for _ in range(n)]
print(bfs((0,0), maps, visited))
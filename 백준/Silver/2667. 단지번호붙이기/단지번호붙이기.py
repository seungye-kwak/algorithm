from collections import deque
n = int(input())
maps = []
for _ in range(n) :
    maps.append([int(x) for x in input()])
    
visited = [[0]*n for _ in range(n)]
def bfs(start, visited, maps) :
    queue = deque([start])
    a, b = start
    visited[a][b] = 1
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    size = 0
    while queue:
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n : 
                if visited[nx][ny] == 0 and maps[nx][ny] == 1 :
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    size += 1
    return size + 1, visited

size_lst = []
for i in range(n) :
    for j in range(n) :
        if maps[i][j] == 1 and visited[i][j] == 0:
            size, visited = bfs((i,j), visited, maps)
            size_lst.append(size)

print(len(size_lst))
print(*sorted(size_lst), sep='\n')
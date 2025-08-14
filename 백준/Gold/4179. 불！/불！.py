from collections import deque
r, c = map(int, input().split())
maps = []
fires = []

for i in range(r):
    row = list(input().strip())
    for j, ch in enumerate(row):
        if ch == 'J':
            start = (i, j)
        elif ch == 'F':
            fires.append((i, j))
    maps.append(row)
        
def fire_bfs(maps, fires) :
    queue = deque()
    visited = [[-1]*c for _ in range(r)]
    for f in fires :
        visited[f[0]][f[1]] = 0
        queue.append(f)
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= r or ny < 0 or ny >= c :
                continue
            
            if visited[nx][ny] == -1 and maps[nx][ny] != '#' :
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
    return visited

fire_time = fire_bfs(maps, fires)

def escape_bfs(maps, start, fire_time) :
    sx, sy = start
    visited = [[-1]*c for _ in range(r)]
    
    # 처음부터 가장자리에 있는 경우
    if sx == 0 or sx == r-1 or sy == 0 or sy == c-1 :
        return 1
    
    queue = deque([start])
    visited[sx][sy] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny <0 or nx>= r or ny >= c :
                continue
            
            nt = visited[x][y] + 1
            
            if visited[nx][ny] == -1 and maps[nx][ny] == '.' :
                # 이동할 수 있는 경우에 불이 더 빠르게 왔으면 이동 불가
                if fire_time[nx][ny] != -1 and fire_time[nx][ny] <= nt :
                    continue
                
                visited[nx][ny] = nt
                
                if nx == 0 or nx == r-1 or ny == 0 or ny == c-1 :
                    return nt + 1
                
                queue.append((nx, ny))
    return 'IMPOSSIBLE'

print(escape_bfs(maps, start, fire_time))
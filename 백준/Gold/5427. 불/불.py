from collections import deque
def fire_bfs(h, w, maps, fires) :
    queue = deque()
    visited = [[-1]*w for _ in range(h)]
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
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w :
                continue
            
            if visited[nx][ny] == -1 and maps[nx][ny] != '#' :
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
    return visited

def escape_bfs(h, w, maps, start, fire_time) :
    sx, sy = start
    visited = [[-1]*w for _ in range(h)]
    
    # 처음부터 가장자리에 있는 경우
    if sx == 0 or sx == h-1 or sy == 0 or sy == w-1 :
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
            
            if nx<0 or ny <0 or nx>= h or ny >= w :
                continue
            
            nt = visited[x][y] + 1
            
            if visited[nx][ny] == -1 and maps[nx][ny] == '.' :
                # 이동할 수 있는 경우에 불이 더 빠르게 왔으면 이동 불가
                if fire_time[nx][ny] != -1 and fire_time[nx][ny] <= nt :
                    continue
                
                visited[nx][ny] = nt
                
                if nx == 0 or nx == h-1 or ny == 0 or ny == w-1 :
                    return nt + 1
                
                queue.append((nx, ny))
    return 'IMPOSSIBLE'
                
    
t = int(input())
for _ in range(t) :
    w, h = map(int, input().split())
    maps = []
    fires = []
    start = (-1, -1)
    for i in range(h) :
        lst = [x for x in input().strip()]
        maps.append(lst)
        for j in range(w) :
            if lst[j] == '@' :
                start = (i, j)
            if lst[j] == '*' :
                fires.append((i, j))
    
    fire_time = fire_bfs(h, w, maps, fires)
    escape_time = escape_bfs(h, w, maps, start, fire_time)
    print(escape_time)
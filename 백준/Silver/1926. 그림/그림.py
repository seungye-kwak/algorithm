n, m = map(int, input().split())
paper = []
for _ in range(n) :
    paper.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

from collections import deque

def bfs(a, b) :
    p = 1
    queue = deque([(a, b)]) # 시작점
    visited[a][b] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue : 
        x, y= queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or nx >=  n or ny < 0 or ny >= m :
                continue
            
            if not visited[nx][ny] and paper[nx][ny] == 1 :
                visited[nx][ny] = True
                queue.append((nx, ny))
                p += 1
    return p

cnt = 0
max_p = 0
for i in range(n) :
    for j in range(m) :
        if paper[i][j] == 1 and not visited[i][j] :
            cnt += 1
            max_p = max(max_p, bfs(i, j))
print(cnt)
print(max_p)
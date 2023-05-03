from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y) :
    queue = deque([(x,y)])
    matrix[x][y] = 0 # 방문처리
    
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx>=m or ny < 0 or ny>=n :
                continue
            
            if matrix[nx][ny] == 1 :
                queue.append((nx, ny))
                matrix[nx][ny] = 0
                
# 행렬 만들기
for i in range(t) :
    m, n, k = map(int, input().split())
    matrix = [[0]*n for _ in range(m)]
    
    cnt = 0
    for j in range(k) :
        x, y = map(int, input().split())
        matrix[x][y] = 1 # 배추 심어진 곳 표시
        
    for a in range(m) :
        for b in range(n) :
            if matrix[a][b] == 1 :
                bfs(a, b)
                cnt += 1
                
    print(cnt)
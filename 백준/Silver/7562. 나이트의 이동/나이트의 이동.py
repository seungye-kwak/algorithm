from collections import deque

def bfs(start, end):
    visited = [[0]*l for _ in range(l)]
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    
    while queue:
        x, y = queue.popleft()
        
        if [x, y] == end:
            return visited[x][y] - 1
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >=l or ny <0 or ny >= l:
                continue
            
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
                
t = int(input())
for _ in range(t) :
    l = int(input()) # 한 변의 길이
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    
    print(bfs(start, end))
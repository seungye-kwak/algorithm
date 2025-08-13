from collections import deque
n = int(input())
picture = []
for _ in range(n) :
    picture.append([x for x in input()])
    
# 적록색약 : 빨강 초록 구분 불가
visited_1 = [[0] * n for _ in range(n)]
visited_2 = [[0] * n for _ in range(n)]
def bfs(start, visited, color=True) :
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue : 
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or nx >= n or ny <0 or ny >= n :
                continue
            
            if color :
                if visited[nx][ny] == 0 and picture[nx][ny] == picture[x][y] :
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
            else :
                if visited[nx][ny] == 0 and (picture[nx][ny] == picture[x][y] or (picture[x][y] == 'R' and picture[nx][ny] == 'G') or (picture[x][y] == 'G' and picture[nx][ny] == 'R')) :
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                
    return visited

cnt = 0
cnt2 = 0
for i in range(n) :
    for j in range(n) :
        if visited_1[i][j] == 0 :
            visited_1 = bfs((i, j), visited_1)
            cnt += 1
        if visited_2[i][j] == 0 :
            visited_2 = bfs((i, j), visited_2, False)
            cnt2 += 1
print(cnt, cnt2)
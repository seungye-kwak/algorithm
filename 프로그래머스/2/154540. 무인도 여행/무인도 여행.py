from collections import deque
def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    maps = [[x for x in m] for m in maps]
    visited = [[0]*m for _ in range(n)]
    # graph = [[-1]*m for _ in range(n)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                q = deque([(i,j)])
                visited[i][j] = 1
                total = max(-1, int(maps[i][j]))
                
                while q:
                    x, y = q.popleft()
                    
                    for d in range(4) :
                        nx = x + dx[d]
                        ny = y + dy[d]
                        
                        if nx < 0 or ny < 0 or nx >=n or ny>=m or maps[nx][ny] == 'X':
                            continue
                        
                        if visited[nx][ny] == 1:
                            continue
                        
                        if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            total += int(maps[nx][ny])
                            q.append((nx,ny))
                answer.append(total)
    if answer == []:
        answer.append(-1)
    return sorted(answer)
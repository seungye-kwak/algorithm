from collections import deque
def solution(board):
    n = len(board)
    m = len(board[0])
    graph = [[x for x in b] for b in board]
    
    # start, end 위치 찾기
    for g in range(n):
        if 'R' in graph[g]:
            start_x, start_y = g, graph[g].index('R')
            
    q = deque([(start_x, start_y, 0)])
    visited = [[0]*m for _ in range(n)]
    visited[start_x][start_y] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q :
        x, y, moves = q.popleft()
        
        if graph[x][y] == 'G':
            return moves
        
        for i in range(4):
            nx, ny = x, y
            
            while True:
                next_x = nx + dx[i]
                next_y = ny + dy[i]
                if next_x < 0 or next_x >= n or next_y < 0 or next_y>=m or graph[next_x][next_y] == 'D':
                    break
                
                nx, ny = next_x, next_y
                
            if not visited[nx][ny] :
                visited[nx][ny] = True
                q.append((nx, ny, moves + 1))
    return -1
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    
    answer = bfs(maps, visited)
    answer = -1 if answer == 1 else answer
    return answer

def bfs(graph, visited) :
    queue = deque([[0,0]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue :
        x,y = queue.popleft()
        visited[x][y] = 1
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or nx >= len(graph) or ny < 0 or ny >= len(graph[0]) :
                continue
            
            if visited[nx][ny] == 1 :
                continue
            
            if graph[nx][ny] == 1 and visited[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
                
    return graph[len(graph)-1][len(graph[0])-1]
        
from collections import deque

def bfs(start, end, graph):
    q = deque([start])
    visited = [[-1] * len(graph[0]) for _ in range(len(graph))]
    visited[start[0]][start[1]] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        x, y = q.popleft()
        
        if (x, y) == end:
            return visited[end[0]][end[1]]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph[0]):
                continue
            
            if visited[nx][ny] != -1:
                continue
            
            if graph[nx][ny] != 'X':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    return -1

def solution(maps):
    # S, L, E 위치 찾기
    for m in range(len(maps)):
        if 'S' in maps[m]:
            start_idx = (m, maps[m].find('S'))
        if 'L' in maps[m]:
            lever_idx = (m, maps[m].find('L'))
        if 'E' in maps[m]:
            end_idx = (m, maps[m].find('E'))

    # 출발지 ~ 레버 거리
    to_lever = bfs(start_idx, lever_idx, maps)
    
    # 레버 ~ 도착지 거리
    to_end = bfs(lever_idx, end_idx, maps)
    
    # 경로가 없는 경우 처리
    if to_lever == -1 or to_end == -1:
        return -1
    else:
        return to_lever + to_end

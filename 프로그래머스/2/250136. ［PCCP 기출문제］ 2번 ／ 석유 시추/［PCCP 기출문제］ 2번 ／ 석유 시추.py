from collections import deque
import sys

def solution(land):
    answer = 0
    visited = [[0]*len(land[0]) for _ in range(len(land))]
    result = {k:0 for k in range(0, len(land[0]))}
    for a in range(len(land)) :
        for b in range(len(land[0])) :
            if land[a][b] == 1 and visited[a][b] == 0:
                max_cnt, columns = bfs((a, b), land, visited)
                for column in columns :
                    result[column] += max_cnt
    answer = max(result.values())

    return answer

def bfs(start, land, visited) :
    a, b = start
    visited[a][b] = 1
    queue = deque([start])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 1
    max_cnt = -sys.maxsize
    columns = []
    
    while queue :
        x, y = queue.popleft()
        columns.append(y)
        max_cnt = max(cnt, max_cnt)

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >= len(land) or ny < 0 or ny >= len(land[0]) :
                continue

            if land[nx][ny] == 0 :
                continue

            if visited[nx][ny] == 0 and land[nx][ny] == 1 :
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = cnt
                columns.append(ny)
            

    return max_cnt, set(columns)
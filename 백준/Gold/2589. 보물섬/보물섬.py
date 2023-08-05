import sys
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

move = [[0,1], [1,0], [-1,0], [0,-1]]

def bfs(x, y) :
    visited = [[0]*m for _ in range(n)]
    q = deque([[x, y]])
    visited[y][x] = 1
    max_=0
    while q :
        x, y = q.popleft()
        for dx, dy in move :
            nx, ny = dx+x, dy+y
            if 0<=nx<m and 0<=ny<n and graph[ny][nx]=='L' and visited[ny][nx] == 0:
                visited[ny][nx]=visited[y][x]+1
                if max_ < visited[ny][nx]:
                    max_ = visited[ny][nx]
                q.append([nx, ny])
    return max_-1

answer = 0
for i in range(n) :
    for j in range(m):
        if graph[i][j] == 'L' :
            tmp = bfs(j, i)
            if tmp>answer :
                answer = tmp
    
print(answer)
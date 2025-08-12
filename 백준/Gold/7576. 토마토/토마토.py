from collections import deque
import sys

m, n = map(int, input().split())

storage = []
starts = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            starts.append((i, j))
    storage.append(row)

visited = [[0]*m for _ in range(n)]

def bfs(starts, visited):
    q = deque(starts)
    for x, y in starts:
        visited[x][y] = 1  # 1일부터 시작 (나중에 -1 해주면 경과일)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if storage[nx][ny] == -1:      # 빈 칸은 그냥 스킵
                continue
            if storage[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited

visited = bfs(starts, visited)

# 최종 판정: 익어야 할 칸(=0)이 끝까지 방문 0이면 실패
max_time = 0
for i in range(n):
    for j in range(m):
        if storage[i][j] == 0 and visited[i][j] == 0:
            print(-1)
            sys.exit(0)
        if visited[i][j] > 0:
            max_time = max(max_time, visited[i][j] - 1)

print(max_time)
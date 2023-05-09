from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    queue = deque([(x, y)])
    land[x][y] = 0  # 방문처리
    while queue:
        x, y = queue.popleft()
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if land[nx][ny] == 1:
                queue.append((nx, ny))
                land[nx][ny] = 0  # 방문처리

while True:
    w, h = map(int, input().split())
    land = []
    cnt = 0
    if (w, h) == (0, 0):
        break

    for _ in range(h):
        land.append(list(map(int, input().split())))

    for a in range(h):
        for b in range(w):
            if land[a][b] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)
from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

graph=[]
for _ in range(n) :
    graph.append([int(x) for x in list(input()) if x != '\n'])

def bfs(x,y) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(x,y)])
    graph[y][x] = 0
    h_cnt = 0
    while queue :
        h_cnt += 1
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n :
                continue
            
            if graph[ny][nx] == 1:
                queue.append((nx, ny))
                graph[ny][nx] = 0
    return h_cnt
    
cnt = 0
h_lst = []
for b in range(n) :
    for a in range(n) :
        if graph[b][a] == 1:
            h_lst.append(bfs(a,b))
            cnt += 1
print(cnt)
h_lst.sort()
for k in h_lst :
    print(k)
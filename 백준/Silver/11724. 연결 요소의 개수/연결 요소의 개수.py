from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

visited = [False]*(n+1)
cnt = 0
for k in range(1, n+1) :
    if not visited[k] :
        if not graph[k] :
            # 방문한 노드가 없을 때
            cnt += 1
            visited[k] = True
        else :
            bfs(graph, k, visited)
            cnt += 1
        
print(cnt)
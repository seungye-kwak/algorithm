from collections import deque

n = int(input()) # 컴퓨터 수
m = int(input()) # 직접 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(g, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
    return sum(visited)-1

print(bfs(graph, 1, visited))
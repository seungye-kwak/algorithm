from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(graph, start, visited) :
    d = dict()
    queue = deque([start])
    while queue :
        v = queue.popleft()
        visited[v] = True
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                d[i] = v
    return d

visited = [False]*(n+1)
result = bfs(graph, 1, visited)

for i in range(2, n+1) :
    print(result[i])
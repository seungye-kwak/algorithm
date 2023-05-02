from collections import deque

n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph :
    i.sort()

# dfs
dfs_v = [False]*(n+1)
def dfs(graph, v, visited) :
    #현재노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
            
# bfs
bfs_v = [False]*(n+1)
def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

dfs(graph, v, dfs_v)
print()
bfs(graph, v, bfs_v)
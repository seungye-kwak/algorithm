from collections import deque

def solution(x, y, n):
    if x == y :
        return 0
    
    visited = [0]*1000001
    graph = [-1]*1000001
    graph[x] = 0
    
    def bfs():
        q = deque([x])
        visited[x] = 1
        
        while q :
            s = q.popleft()
            
            for num in [s*3, s*2, s+n] :
                if num > 1000000 :
                    continue
                if visited[num] == 0:
                    graph[num] = graph[s] + 1
                    visited[num] = 1
                    q.append(num)
                    
                if num == y:
                    return graph[num]
        return -1
    return bfs()
import sys
from collections import deque

F, S, G, U, D = map(int, input().split())

bfs_v = [0]*(F+1)                
def bfs(s, g) :
    queue = deque([s])
    bfs_v[s] = True
    
    while queue :
        n = queue.popleft()
        
        if n == g :
            return bfs_v[n] -1 # 첫 시작층 제외
        
        for i in (n+U, n-D) :
            if 0 < i <= F and bfs_v[i] == 0 :
                queue.append(i)
                bfs_v[i] = bfs_v[n] + 1
                
    return 'use the stairs'

print(bfs(S, G))
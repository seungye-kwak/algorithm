import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(m+2)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
if graph[1] == [] :
    print(0)
else :
    lst = []
    for i in graph[1] :
        lst = lst + graph[i]
    lst = set(lst + graph[1])
    print(len(lst)-1)
t = int(input())

def cycle(lst) :
    cnt = 0
    for i in range(1, len(lst)) :
        if not visited[i] :
            visited[i] = True
            next = lst[i]
            while next != i :
                visited[next] = True
                next = lst[next]
            cnt += 1
    return cnt

for _ in range(t) :
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    visited = [False]*(n+1)
    print(cycle(lst))
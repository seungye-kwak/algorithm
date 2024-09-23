def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for x in range(n) :
        if visited[x] == False:
            dfs(n, computers, x, visited)
            answer += 1
    return answer

def dfs(n, computers, start, visited) :
    visited[start] = True
    for i in range(n) :
        if i != start and computers[start][i] == 1 :
            if visited[i] == False :
                dfs(n, computers, i, visited)
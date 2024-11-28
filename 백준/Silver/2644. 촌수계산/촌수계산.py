from collections import deque

n = int(input())
a, b = map(int, input().split())
num = int(input())

# 가족 관계 그래프 초기화
family = [[] for _ in range(n+1)]
for _ in range(num):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

# BFS 함수 정의
def bfs(a, b):
    q = deque([(a, 0)])  # 큐에 (노드, 현재 촌수) 저장
    visited = [0] * (n + 1)  # 방문 여부 초기화
    visited[a] = 1  # 시작 노드 방문 처리
    
    while q:
        current, cnt = q.popleft()
        
        # 종료 조건: 현재 노드가 b인 경우
        if current == b:
            return cnt
        
        # 현재 노드의 인접 노드 탐색
        for neighbor in family[current]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1  # 방문 처리
                q.append((neighbor, cnt + 1))  # 촌수 증가하며 큐에 추가

    return -1  # b에 도달할 수 없는 경우

# 결과 출력
print(bfs(a, b))

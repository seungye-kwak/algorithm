n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 3차원 DP 테이블: dp[행][열][방향]
# 방향 0: 왼쪽 대각선, 1: 아래, 2: 오른쪽 대각선
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]

# 첫 번째 행 초기화 (직전 방향은 의미가 없으므로 각 방향에 같은 값을 넣음)
for j in range(m):
    for k in range(3):
        dp[0][j][k] = graph[0][j]

# DP 계산
for i in range(1, n):
    for j in range(m):
        # 왼쪽 대각선에서 오는 경우 (직전 방향이 2가 아니어야 함)
        if j > 0:
            dp[i][j][0] = min(dp[i][j][0], dp[i-1][j-1][1], dp[i-1][j-1][2]) + graph[i][j]
        # 바로 위에서 오는 경우 (직전 방향이 1이 아니어야 함)
        dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][0], dp[i-1][j][2]) + graph[i][j]
        # 오른쪽 대각선에서 오는 경우 (직전 방향이 0이 아니어야 함)
        if j < m - 1:
            dp[i][j][2] = min(dp[i][j][2], dp[i-1][j+1][0], dp[i-1][j+1][1]) + graph[i][j]

# 마지막 행에서 최소값 구하기
result = float('inf')
for j in range(m):
    result = min(result, dp[-1][j][0], dp[-1][j][1], dp[-1][j][2])

print(result)

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

# 오른쪽, 아래, 오른쪽 아래 대각선
# 회전은 45도로만 시킬 수 있다.
dp = [[[0]*n for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(n) :
        if house[i][j] == 1:
            continue
        
        # 오른쪽 가로 이동
        if j+1 < n and house[i][j+1] == 0:
            # 파이프 이동 방향이 가로일 때는 이전에 이동 방향이 오른쪽 혹은 오른쪽 아래 대각선일 때
            dp[i][j+1][0] += dp[i][j][0] + dp[i][j][2]
        if i+1 < n and house[i+1][j] == 0:
            dp[i+1][j][1] += dp[i][j][1] + dp[i][j][2]
        if i+1 < n and j+1 < n and house[i+1][j] ==0 and house[i+1][j+1] == 0 and house[i][j+1] == 0:
            dp[i+1][j+1][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
            
print(sum(dp[n-1][n-1]))
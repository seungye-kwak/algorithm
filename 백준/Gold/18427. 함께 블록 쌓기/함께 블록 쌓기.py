N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (H + 1)
dp[0] = 1  # 높이 0을 만드는 방법은 1가지 (아무것도 안 쌓는 경우)

MOD = 10007  # 나머지 연산

for i in range(N):
    new_dp = dp[:]  # 현재 상태 복사
    for b in blocks[i]:
        for h in range(H - b + 1):
            new_dp[h + b] = (new_dp[h + b] + dp[h]) % MOD
    dp = new_dp  # 업데이트

print(dp[H])
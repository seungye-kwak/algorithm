n = int(input())
dp = [0] * (n + 1)
prev = [0] * (n + 1)

# base
if n >= 1:
    dp[1] = 0
    prev[1] = 0

for i in range(2, n + 1):
    # 기본 후보: i-1
    dp[i] = dp[i - 1] + 1
    prev[i] = i - 1

    # 3으로 나눠지는 경우
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

    # 2로 나눠지는 경우
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2

print(dp[n])

# 경로 복원
path = []
cur = n
while cur:
    path.append(cur)
    if cur == 1:
        break
    cur = prev[cur]
print(*path)
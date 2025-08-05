n, k = map(int, input().split())
backpack = []
for i in range(n) :
    w, v = map(int, input().split())
    backpack.append((w, v))
    
backpack.sort(key = lambda x: (x[1], -x[0]), reverse=True)

dp = [0] * (k+1)
for w, v in backpack :
    for i in range(k, w-1, -1) :
        # 7, 6
        dp[i] = max(dp[i], dp[i-w] + v) # dp[7] = max(dp[7], dp[1] + 13), dp[6] = max(dp[6], dp[0] + 13)
print(dp[k])
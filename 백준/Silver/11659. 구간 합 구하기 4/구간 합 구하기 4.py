import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * (n+1)
dp[0] = nums[0]
for i in range(1, n) :
    dp[i] = dp[i-1] + nums[i]
    
for _ in range(m) :
    a, b = map(int, input().split())
    if a == 1 :
        print(dp[b-1])
    elif a == b :
        print(nums[b-1])
    else :
        print(dp[b-1] - dp[a-2])
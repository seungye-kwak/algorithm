n, d = map(int, input().split())
way = []
for _ in range(n):
    start, end, length = map(int, input().split())
    if (length < end-start) and end <= d:
        way.append((start, end, length))
way.sort()

dp = [i for i in range(d+1)]
for s, e, l in way:
    for x in range(d+1):
        if e == x :
            dp[x] = min(dp[x], dp[s] + l)
        else :
            dp[x] = min(dp[x], dp[x-1]+1)
            
print(dp[-1])
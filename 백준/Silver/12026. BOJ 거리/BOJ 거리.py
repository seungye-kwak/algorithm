import sys
input = sys.stdin.readline
n = int(input())
blocks = input().strip()

INF = float('inf') # 무한대 값 설정
dp = [INF] * n
dp[0] = 0

def next_step(start, end):
    if start == 'B' and end == 'O':
        return True
    if start == 'O' and end == 'J':
        return True
    if start == 'J' and end == 'B':
        return True
    
    return False

for i in range(1, n):
    # i == 1
    for j in range(i):
        # j = [0]
        if next_step(blocks[j], blocks[i]):
            # next_step(dp[0], dp[1])
            dp[i] = min(dp[i], dp[j] + (i-j) ** 2)
            
if dp[n-1] == INF:
    print(-1)
else:
    print(dp[n-1])
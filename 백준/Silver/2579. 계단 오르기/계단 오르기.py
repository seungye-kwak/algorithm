n = int(input())
stairs = [0]
for i in range(n):
    stairs.append(int(input()))
    
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안된다. 단, 시작점은 포함되지 않음
# 마지막 도착 계단은 반드시 밟아야 함

if n==1:
    print(stairs[1])
elif n==2 :
    print(stairs[1]+stairs[2])
else:
    dp = [0] * (n+1)
    dp[1] = stairs[1]
    dp[2] = stairs[1]+stairs[2]
    dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])
    
    
    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3]+stairs[i-1]) + stairs[i]
        
    print(dp[n])
from collections import deque

n, k = map(int, input().split())
belt = list(map(int, input().split()))

robots = deque([False]*(2*n)) # True 는 로봇이 있음

step = 0
while True:
    step += 1
    
    # 1. 벨트가 회전한다.
    belt = [belt[-1]] + belt[:-1]
    robots.rotate(1) # deque의 이동 함수
    robots[n-1] = False # 내리는 위치(n번째칸)에는 로봇을 내림
    
    # 2. 로봇을 이동시킨다. (뒤에서부터)
    for i in range(n-2, -1, -1) :
        if robots[i] and not robots[i+1] and belt[i+1] > 0 :
            robots[i] = False
            robots[i+1] = True
            belt[i+1] -= 1
            
    robots[n-1] = False # 내리는 위치에 있으면 내린다.
    
    # 3. 로봇을 올린다.
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1 # 내구도 감소
        
    if belt.count(0) >= k:
        break
    
print(step)
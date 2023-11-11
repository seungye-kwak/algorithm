from collections import deque
def right(idx, d) :# 오른쪽 톱니바퀴 확인
    if idx > 3:
        # 4번째 바퀴는 확인 안 함
        return
    
    # 같은 극이 아니면 회전
    if g[idx-1][2] != g[idx][6] :
        right(idx+1, -d)
        g[idx].rotate(d)
        
def left(idx, d) :
    if idx < 0 :
        return
    # 같은 극이 아니면 회전
    if g[idx][2] != g[idx+1][6] :
        left(idx-1, -d)
        g[idx].rotate(d)
        
# 톱니바퀴 4개 입력받기
g = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input()) # 회전 횟수

for _ in range(k) :
    # 회전할 바퀴 인덱스, 회전방향 입력받기
    idx, d = map(int, input().split())
    idx -=1 # 인덱스이기 때문에
    
    # -d : 회전할 톱니번호가 회전하는 방향의 반대방향으로 회전해야 하기 때문
    left(idx-1, -d)
    right(idx+1, -d)
    
    # 회전할 톱니 번호의 톱니도 회전
    g[idx].rotate(d)
    
# 점수 계산
score = 0
for i in range(4) :
    if g[i][0] == 1:
        score += 2 ** i
        
print(score)
    
    
from collections import deque
import sys
input = sys.stdin.readline

# 사무실의 세로(N), 가로(M)
N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

# 남, 동, 북, 서 방향을 가리킴 (남쪽을 시작으로 반시계방향으로 돌아가는 순서로 되어 있음)
dy = [1, 0, -1, 0]       # y축
dx = [0, 1, 0, -1]       # x축

# 감시해야하는 모든 방향 (각각의 cctv별로 감시할 수 있는 방향)
direction = {
    1: [[0], [1], [2], [3]], 
    2: [[0, 2], [1, 3]],                   
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],    
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]                    
}

# 사무실의 범위를 벗어나는지 체크
def check(row, col):
    return row < 0 or row >=N or col < 0 or col >=M
    

def init():
    obj = deque() #  cctv의 위치를 저장할 큐 
    answer = 0
    for i in range(N):
        for j in range(M):
            # 벽이아니고 빈칸이아니면 
            if space[i][j] != 6 and space[i][j] != 0:
                obj.append((space[i][j], i, j))   # cctv번호, cctv 좌표 저장
            # cctv가 아에 없는 경우도 고려해서 빈칸의 갯수로 맞춰둠
            if space[i][j] == 0:answer += 1
    return obj, answer

# cctv좌표들, 빈칸 개수 초기화
cctv, answer = init()


def move(y, x, direc, space_copy):
    # 각각의 방향에 대해서 전부 이동시켜줌
    for d in direc:
        ny, nx = y, x
        
        while True:
            nx += dx[d]
            ny += dy[d]
            # 범위를 벗어났거나 벽을 만났다면 
            if check(ny, nx) or space_copy[ny][nx] == 6:
                break
            # 빈칸이아니면 
            if space_copy[ny][nx] != 0:
                continue
            space_copy[ny][nx] = '#'


# 사각지대를 구하는 함수        
def zero_cnt(space_copy):
    global answer
    cnt = 0
    for i in space_copy:
        cnt += i.count(0)
    answer = min(answer, cnt) 
    

# 백준 15651 N과 M(3) 문제와 유사 (백트래킹)
def dfs(level, space):
    # space_copy = copy.deepcopy(space)           
    space_copy = [[j for j in space[i]] for i in range(N)]
    # 2번째 상태가 실행되기전 바로 전 상태를 저장함 
    # (예를 들어 2번째 상태를 시작하기 전에 1번째 상태의 결과를 저장함)
   
    if level == len(cctv):
        zero_cnt(space_copy)
        return			# 전 상태로 돌아감
    
    number, y, x  = cctv[level]
    
    # number번째 cctv에 대해 가능한 모든 방향을 순차적으로 고려 
    for d in direction[number]:    
        move(y, x, d, space_copy)
        dfs(level+1, space_copy)   # level+1번째 cctv를 고려
        space_copy = [[j for j in space[i]] for i in range(N)]
        # space_copy = copy.deepcopy(space)
        
        # 하나의 상태를 return 한다음 바로 전 상태로 바꿈 
        # 만약 2번째 상태가 끝났다면,  1번째를 수행했을 때의 결과로 바꿈
    
dfs(0, space)
print(answer)
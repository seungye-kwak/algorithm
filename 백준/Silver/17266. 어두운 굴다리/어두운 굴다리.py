import heapq

N = int(input()) #굴다리 길이
M = int(input()) # 가로등 개수
loc = list(map(int, input().split())) #M개의 설치할 수 있는 가로등 위치 x

def light_range(n, positions, height):
    cur_pos = 0
    for pos in positions :
        if pos - height > cur_pos :
            return False #커버할 수 없는 위치 발생
        cur_pos = pos + height
        
    return cur_pos >= N

left, right = 0, N
result = N

while left <= right:
    mid = (left+right) // 2
    if light_range(N, loc, mid):
        result = mid
        right = mid - 1
        
    else :
        left = mid + 1
        
print(result)
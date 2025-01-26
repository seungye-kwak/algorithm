import heapq

N = int(input()) #굴다리 길이
M = int(input()) # 가로등 개수
loc = list(map(int, input().split())) #M개의 설치할 수 있는 가로등 위치 x

def light_range(n, positions, height):
    heap = []
    for pos in positions:
        heapq.heappush(heap, (pos-height, pos+height))
    
    cur_pos = 0
    while heap:
        start, end = heapq.heappop(heap)
        if start > cur_pos:
            return False
        cur_pos = max(cur_pos, end)
        if cur_pos >= n:
            return True
        
    return cur_pos >= n

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
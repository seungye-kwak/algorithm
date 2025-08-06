import heapq
import sys

input = sys.stdin.readline 
n = int(input())

left = []
right = []
for _ in range(n) :
    num = int(input())
    if not left or num <= -left[0] :
        heapq.heappush(left, -num)
    else :
        heapq.heappush(right, num)
    
    # 힙 크기 균형 조정 (left가 항상 크거나 같도록)
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    # 중앙값 출력
    print(-left[0])
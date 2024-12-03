import heapq
def solution(n, k, enemy):
    heap = []
    for i, e in enumerate(enemy):
        heapq.heappush(heap, -e)
        n-=e
        
        if n < 0:
            # 남은 병사가 없고
            if k > 0:
                # 무적권이 남아 있으면
                # 지금껏 상대했던 적 중에 가장 많은 적 때 무적권 사용
                n += -heapq.heappop(heap)
                k -= 1
            else:
                return i # 현재 라운드 반환
            
    return len(enemy)
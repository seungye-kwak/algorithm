import heapq

heap=[]
n = int(input())

for _ in range(n) :
    n_lst = map(int, input().split())
    for i in n_lst :
        if len(heap) < n :
            heapq.heappush(heap, i)
            
        else :
            if heap[0] < i :
                heapq.heappop(heap)
                heapq.heappush(heap, i)
                
print(heap[0])
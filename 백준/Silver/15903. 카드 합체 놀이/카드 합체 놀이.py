import sys
from heapq import heapify, heappop, heappush
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
n_lst = list(map(int, input().split()))

heapify(n_lst)

for _ in range(m) :
    a = heappop(n_lst)
    b = heappop(n_lst)
    
    heappush(n_lst, a+b)
    heappush(n_lst, a+b)
    
print(sum(n_lst))
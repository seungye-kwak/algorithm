import sys
from heapq import heapify, heappop, heappush
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
n_lst = list(map(int, input().split()))

for _ in range(m) :
    n_lst.sort()
    n_lst[0] = n_lst[1] = n_lst[0]+n_lst[1]
    
print(sum(n_lst))
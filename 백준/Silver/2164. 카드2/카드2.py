import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([x for x in range(1, n+1)])

for _ in range(n) :
    if len(queue)>1 :
        queue.popleft()
        queue.append(queue.popleft())
    else :
        print(queue[0])
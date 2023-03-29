import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])
for _ in range(n) :
    msg = list(input().split())
    if msg[0]=='push':
        queue.append(msg[1])
    elif msg[0]=='pop':
        if queue :
            print(queue.popleft())
        else :
            print(-1)
    elif msg[0]=='size':
        print(len(queue))
    elif msg[0]=='empty':
        if queue :
            print(0)
        else :
            print(1)
    elif msg[0]=='front':
        if queue :
            print(queue[0])
        else :
            print(-1)
    else :
        if queue :
            print(queue[-1])
        else :
            print(-1)
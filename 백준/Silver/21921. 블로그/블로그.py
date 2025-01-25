from collections import deque

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

v_lst = deque([])
v = 0
max_v = 0
days = 0
total = []
for i in range(n):
    if days < x :
        days += 1
        v_lst.append(visitors[i])
        v += visitors[i]
    
    if days == x:
        max_v = max(max_v, v)
        total.append(v)
        v = v -v_lst.popleft()
        days -= 1
        
        
if max_v == 0:
    print('SAD')
else:     
    print(max_v)
    print(total.count(max_v))

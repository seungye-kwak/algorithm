p, m = map(int, input().split())

rooms = []
for i in range(p) :
    l, n = input().split()
    l = int(l)
    
    status = False
    for r in rooms:
        cut = r[0][0]
        if cut -10 <= l <= cut + 10:
            if len(r) < m:
                r.append((l, n))
                status = True
                break
        
    if not status:
        rooms.append([(l, n)])
        
for r in rooms :
    if len(r) == m:
        print('Started!')
            
    else:
        print('Waiting!')
        
    r.sort(key=lambda x: x[1])
    for p in r:
        print(*p)
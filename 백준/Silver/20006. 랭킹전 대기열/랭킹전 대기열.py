p, m = map(int, input().split())

rooms = {}
for i in range(p) :
    l, n = input().split()
    l = int(l)
  
    status = False
    for r in rooms.keys():
        key = rooms[r][0]
        if key-10 <= l <= key+10:
            if len(rooms[r][1]) < m:
                rooms[r][1].append((l, n))
                status = True
                break 
        
    if status == False:
        rooms[n] = [l, [(l, n)]]
        
for k, v in rooms.items() :
    if len(v[1]) == m:
        print('Started!')
            
    else:
        print('Waiting!')
        
    v[1].sort(key=lambda x: x[1])
    for p in v[1]:
        print(*p)
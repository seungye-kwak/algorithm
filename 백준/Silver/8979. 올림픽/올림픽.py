n, k = map(int, input().split())
d = []
for _ in range(n) :
    i, g, s, b = map(int, input().split())
    d.append((i, g, s, b))
    
d.sort(key=lambda x: (-x[1], -x[2], -x[3]))

prev_rank = 0
prev_medal = None
rank = {}
for i, (idx, g, s, b) in enumerate(d) :
    medal = (g, s, b)
    if i == 0 :
        prev_rank = 1
    else :
        if medal != prev_medal :
            prev_rank = i+1
    rank[idx] = prev_rank
    prev_medal = medal
    
print(rank[k])
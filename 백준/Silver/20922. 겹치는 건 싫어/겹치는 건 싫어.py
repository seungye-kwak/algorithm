n, k = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, 0
dupl = dict()
max_cnt = 0

while end < n :
    if lst[end] not in dupl :
        dupl[lst[end]] = 0
        
    if dupl[lst[end]] != k :
        dupl[lst[end]] += 1
        end += 1
        
    else :
        dupl[lst[start]] -= 1
        start += 1
        
    max_cnt = max(max_cnt, end-start)

print(max_cnt)
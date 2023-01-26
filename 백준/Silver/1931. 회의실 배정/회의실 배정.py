n = int(input())
total_meet = []
for _ in range(n) :
    s, e = map(int, input().split())
    total_meet.append([s, e])
#정렬
total_meet.sort(key=lambda x: (x[1], x[0]))
cnt = 0
start = 0
end = 0
for m in total_meet :
    if m[0] >= end :
        cnt+=1
        start = m[0]
        end=m[1]
print(cnt)
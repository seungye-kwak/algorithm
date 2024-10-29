n, m = map(int,input().split())
lst = [0]*n
for _ in range(m):
    a, z, num = map(int, input().split())
    for i in range(a, z+1):
        lst[i-1] = num
        
print(*lst)
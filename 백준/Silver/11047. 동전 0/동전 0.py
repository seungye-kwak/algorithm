n, k = map(int, input().split())
c_lst = []
for _ in range(n) :
    c_lst.append(int(input()))
    
cnt = 0
for i in reversed(range(n)) :
    i_cnt, etc = divmod(k, c_lst[i])
    cnt+=i_cnt
    k = etc
    
print(cnt)
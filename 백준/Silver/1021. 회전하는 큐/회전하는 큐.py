from collections import deque

n, m = map(int, input().split())
lst = list(map(int, input().split()))
n_lst = deque([x for x in range(1, n+1)])

second = 0
third=0
for i in lst :
    while i != n_lst[0] :
        if n_lst.index(i) <= (len(n_lst)//2) :
            a = n_lst.popleft()
            n_lst.append(a)
            second += 1
        else :
            a = n_lst.pop()
            n_lst.appendleft(a)
            third += 1
    n_lst.popleft()
print(second + third)
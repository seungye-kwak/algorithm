from itertools import combinations

n, m = map(int, input().split())
n_lst = [x for x in range(1,n+1)]

comb = list(combinations(n_lst, m))

for i in comb :
    for j in i :
        print(j, end=' ')
    print()
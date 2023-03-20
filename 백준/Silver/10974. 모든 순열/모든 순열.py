from itertools import permutations

n = int(input())
n_lst = [x for x in range(1, n + 1)]
n_p_lst = list(permutations(n_lst, n))

for i in n_p_lst:
    for j in i:
        print(j, end=" ")
    print()
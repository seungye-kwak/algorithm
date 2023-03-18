from itertools import combinations

while True :
    num_lst = list(map(int, input().split()))
    if num_lst[0] == 0 :
        break
    del num_lst[0]
    
    six_lst = list(combinations(num_lst, 6))
    
    for i in six_lst :
        for j in i :
            print(j, end=' ')
        print()
    print()
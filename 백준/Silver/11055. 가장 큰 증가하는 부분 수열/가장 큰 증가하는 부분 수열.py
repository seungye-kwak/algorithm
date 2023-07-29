n = int(input())
lst = list(map(int, input().split()))
sum_lst = lst[:]

for i in range(1, n):
    for j in range(i):
        if lst[j] < lst[i]:
            sum_lst[i] = max(sum_lst[i], sum_lst[j] + lst[i])
            # i = 1 일 때
            # sum_lst[1] = max(sum_lst[1], sum_lst[0]+lst[1]) = 101

            # i = 2 일 때
            # sum_lst[2] = max(sum_lst[2], sum_lst[0]+lst[2]) = 3

            # i = 3 일 때
            # sum_lst[3] = max(sum_lst[3], sum_lst[0]+lst[3]) = 51
            # sum_lst[3] = max(sum_lst[3], sum_lst[2]+lst[3]) = 53

            # i = 4일 때
            # sum_lst[4] = max(sum_lst[4], sum_lst[0]+lst[4]) = 61
            # sum_lst[4] = max(sum_lst[4], sum_lst[2]+lst[4]) = 63
            # sum_lst[4] = max(sum_lst[4], sum_lst[3]+lst[4]) = 113

print(max(sum_lst))
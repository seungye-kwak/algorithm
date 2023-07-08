lst = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]
while True :
    for i in range(len(lst)-1) :
        if lst[i] > lst[i+1] :
            lst[i], lst[i+1] = lst[i+1], lst[i]
            print(*lst)
    if lst==answer :
        break
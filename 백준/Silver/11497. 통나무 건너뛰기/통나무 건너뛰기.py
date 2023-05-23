T = int(input())

def min_hight(lst):
    if lst.count(lst[0]) == n:
        return 0

    lst = sorted(lst)
    high = []
    for i in range(len(lst) - 1):
        if i == len(lst) - 2:
            high.append(abs(lst[i] - lst[i + 1]))
        else:
            if i == 0:
                high.append(abs(lst[i] - lst[i + 1]))
            high.append(abs(lst[i] - lst[i + 2]))

    return max(high)


while T:
    n = int(input())
    lst = list(map(int, input().split()))

    print(min_hight(lst))
    T -= 1
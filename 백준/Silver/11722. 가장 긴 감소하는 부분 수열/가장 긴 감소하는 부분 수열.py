n = int(input())
lst = list(map(int, input().split()))
length = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if lst[j] > lst[i]:
            length[i] = max(length[i], length[j] + 1)

print(max(length))
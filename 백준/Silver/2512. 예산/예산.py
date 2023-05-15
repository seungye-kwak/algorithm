import sys

input = sys.stdin.readline
n = int(input())  # 3<=n<=10000
lst = list(map(int, input().split()))
lst = sorted(lst)
m = int(input())

for i in lst:
    if n == 1:
        print(i)
    else:
        if m / n <= i:
            print(int(m / n))
            break
        m -= i
        n -= 1
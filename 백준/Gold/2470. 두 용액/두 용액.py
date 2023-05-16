import sys

input = sys.stdin.readline
n = int(input())  # 2<=ㅜ<=100000 : 전체 용액의 수
lst = sorted(list(map(int, input().split())))

start, end = 0, n - 1
ans = abs(lst[start] + lst[end])
final = [lst[start], lst[end]]

while start < end:
    left = lst[start]
    right = lst[end]

    sum = left + right

    if abs(sum) < ans:
        ans = abs(sum)
        final = [left, right]
        if ans == 0:
            break

    if sum < 0:
        start += 1
    else:
        end -= 1

print(*final)
import sys

input = sys.stdin.readline
n = int(input())  # 1 <= n <= 3**7
paper = [list(map(int, input().split())) for _ in range(n)]
result = []


def solution(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                solution(x, y, n // 3)
                solution(x, y + n // 3, n // 3)
                solution(x, y + n // 3 * 2, n // 3)
                solution(x + n // 3, y, n // 3)
                solution(x + n // 3, y + n // 3, n // 3)
                solution(x + n // 3, y + n // 3 * 2, n // 3)
                solution(x + n // 3 * 2, y, n // 3)
                solution(x + n // 3 * 2, y + n // 3, n // 3)
                solution(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return
    if color == 0:
        result.append(0)
    elif color == -1:
        result.append(-1)
    else:
        result.append(1)


solution(0, 0, n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
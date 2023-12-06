import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
result = 1000000

house = []
chicken =[]
for i in range(N) :
    for j in range(N) :
        if city[i][j] == 1 :
            house.append([i,j]) # 집 좌표 추가
        elif city[i][j] == 2 :
            chicken.append([i,j])
            
for chi in combinations(chicken, M):
    temp = 0
    for h in house :
        default = 101
        for k in range(M) :
            default = min(default, abs(h[0]-chi[k][0]) + abs(h[1]-chi[k][1]))
        temp += default
    result = min(result, temp)
    
print(result)
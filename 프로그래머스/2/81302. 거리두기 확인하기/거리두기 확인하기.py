from itertools import product
from collections import deque

def check_place(place):
    people = [(i, j) for i in range(5) for j in range(5) if place[i][j] == 'P']
    
    # 각 사람 위치 간 거리 확인
    for i, (x1, y1) in enumerate(people):
        for j, (x2, y2) in enumerate(people):
            if i >= j:  # 중복 검사 방지
                continue
            
            dist = abs(x1 - x2) + abs(y1 - y2)
            if dist > 2:
                continue  # 거리 2 초과는 검사하지 않음
            
            # 거리 1: 무조건 위반
            if dist == 1:
                return 0
            
            # 거리 2: 경로에 파티션 확인
            if dist == 2:
                # 대각선
                if x1 != x2 and y1 != y2:
                    if place[x1][y2] != 'X' or place[x2][y1] != 'X':
                        return 0
                # 직선
                else:
                    if x1 == x2:  # 같은 행
                        if place[x1][(y1 + y2) // 2] != 'X':
                            return 0
                    if y1 == y2:  # 같은 열
                        if place[(x1 + x2) // 2][y1] != 'X':
                            return 0
    return 1

def solution(places):
    result = []
    for place in places:
        result.append(check_place(place))
    return result
def solution(friends, gifts):
    matrix = [[0]*len(friends) for _ in range(len(friends))]
    d = dict(zip(friends, [x for x in range(len(friends))]))
    # 선물 주고받은 메트릭스 만들기
    for g in gifts :
        give, get = g.split(' ')[0], g.split(' ')[1] 
        matrix[d[give]][d[get]] += 1
        
    # 이번 달에 주고받은 선물이 있는지 확인하기
    new_matrix = [0] * len(friends)
    for x in range(len(friends)) :
        for y in range(len(friends)):
            if matrix[x][y] > matrix[y][x] :
                # x가 y에게 준 선물이 더 많을 경우
                new_matrix[x] += 1 # 다음 달에 선물을 하나 더 받음
                
            elif matrix[x][y]==matrix[y][x] :
                # 주고 받은 수가 같거나 둘다 0일 경우
                x_idx = sum(matrix[x]) - sum(i[x] for i in matrix)
                y_idx = sum(matrix[y]) - sum(i[y] for i in matrix)
                
                if x_idx > y_idx :
                    new_matrix[x] += 1
                    
    return max(new_matrix)


def solution(land):
    score = land # 행을 거쳐 값을 누적함
    for i in range(1,len(land)) :
        for j in range(4) :
            score[i][j] += max(score[i-1][:j]+score[i-1][j+1:]) # 해당 인덱스 제외하고 최대값을 더해줌
            
    answer = max(score[len(land)-1]) # 마지막 행의 최대값이 더해진 최고점이 됨       

    return answer
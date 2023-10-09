def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    
    e = 0
    for t in targets :
        if t[0] >= e :
            answer += 1
            e = t[1] 
    return answer
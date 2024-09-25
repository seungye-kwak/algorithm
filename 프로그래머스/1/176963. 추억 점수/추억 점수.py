def solution(name, yearning, photo):
    answer = []
    d = dict(zip(name, yearning))
    for p in photo :
        result = 0
        for i in p :
            if i in d.keys():
                result += d[i]
        answer.append(result)
        
    return answer
def solution(data, ext, val_ext, sort_by):
    value_name=['code', 'date', 'maximum', 'remain']
    answer = [] # 코드 번호, 제조일, 최대수량, 현재수량
    cond = value_name.index(ext)
    sort_ = value_name.index(sort_by)
    for d in data :
        if d[cond] < val_ext :
            answer.append(d)
        
    answer.sort(key=lambda x : x[sort_])
    
    return answer
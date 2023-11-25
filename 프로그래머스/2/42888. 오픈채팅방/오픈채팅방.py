def solution(record):
    result = {}
    for x in record :
        x_lst = x.split(' ')
        if x_lst[0] != 'Leave':
            result[x_lst[1]] = x_lst[2]
        
    answer = []
    for x in record :
        x_lst = x.split(' ')
        if x_lst[0] == 'Enter':
            answer.append(f"{result[x_lst[1]]}님이 들어왔습니다.")
        elif x_lst[0] == 'Leave':
            answer.append(f"{result[x_lst[1]]}님이 나갔습니다.")
        else :
            pass
    return answer
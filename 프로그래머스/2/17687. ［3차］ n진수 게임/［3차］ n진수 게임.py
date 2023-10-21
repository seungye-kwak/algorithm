def convert(n, base) :
    arr='0123456789ABCDEF'
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else :
        return convert(q, base) + arr[r]
    
def solution(n, t, m, p) :
    answer = ''
    all_turn = ''
    for i in range(m*t) :
        all_turn += str(convert(i, n))
        
    while len(answer) < t:
        answer += all_turn[p-1]
        p += m
    return answer
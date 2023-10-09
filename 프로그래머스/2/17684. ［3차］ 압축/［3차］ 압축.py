import string

def solution(msg):
    upper = [i for i in string.ascii_uppercase]
    d = dict(zip(upper, list(range(1, 27))))
    
    i = 0
    check = ''
    result = []
    num = 27
    
    while i < len(msg):
        check += msg[i]
        if check in d:
            i+=1
        else:
            d[check] = num
            num += 1
            result.append(d[check[:-1]])
            check = ''
    result.append(d[check])
    return result
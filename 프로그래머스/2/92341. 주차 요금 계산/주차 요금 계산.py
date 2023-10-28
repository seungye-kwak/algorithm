import math

def str_to_time(str_time) :
    h, m = str_time.split(':')
    total_m = int(h)*60+int(m)
    return total_m

def solution(fees, records):
    d = dict()
    dt, dp, ut, up = fees
    
    for i in records :
        t, c, io = i.split(' ')
        if c in d.keys() :
            d[c].append([str_to_time(t), io])
        else :
            d[c] = [[str_to_time(t), io]]
            
    item = list(d.items())
    item.sort(key = lambda x: x[0])
    
    answer = []
    for car in item :
        total_time = 0
        for x in range(len(car[1])):
            if x == len(car[1])-1 and car[1][x][1] == 'IN' :
                out_time = str_to_time('23:59')
                total_time += out_time - car[1][x][0]
            if car[1][x][1] == 'OUT':
                total_time += car[1][x][0] - car[1][x-1][0]
                
        if total_time <= dt :
            answer.append(dp)
        else :
            answer.append(dp+math.ceil((total_time-dt)/ut)*up)
    
    return answer
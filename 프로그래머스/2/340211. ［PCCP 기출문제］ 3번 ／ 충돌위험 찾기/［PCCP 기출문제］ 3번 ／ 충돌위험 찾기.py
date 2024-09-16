
def solution(points, routes) :
    def move(route) :
        total = []
        for x in range(len(route)-1) :
            start = points[route[x]-1]
            end = points[route[x+1]-1]
            move_num = [end[0]-start[0], end[1]-start[1]]

            if x == 0 :
                total.append(start)

            for i in range(abs(move_num[0])+abs(move_num[1])) :
                if move_num[0] > 0 :
                    start = [start[0] + 1, start[1]]
                    move_num[0] -= 1
                elif move_num[0] < 0 :
                    start = [start[0] - 1, start[1]]
                    move_num[0] += 1
                else :
                    if move_num[1] > 0 :
                        start = [start[0], start[1]+1]
                        move_num[1] -= 1
                    elif move_num[1] < 0 :
                        start = [start[0], start[1]-1]
                        move_num[1] += 1
                    else :
                        pass
                total.append(start)
        return total
    
    answer = 0
    total_route = []
    max_length = 0
    for route in routes :
        route_idx = move(route)
        total_route.append(route_idx)
        max_length = max(max_length, len(route_idx))
        
    for i in range(max_length):
        lst = []
        for x in range(len(total_route)) :
            if i < len(total_route[x]) :
                value = total_route[x][i]
                lst.append(f'{value[0]}-{value[1]}')
        
        answer += len(set([x for x in lst if lst.count(x)>1]))
        
    return answer
def solution(park, routes):
    answer = 0
    # S:시작지점, O:이동 가능한 통로, X: 장애물
    w = len(park[0])
    h = len(park)
    maps = [[x for x in p] for p in park]
    
    # 시작지점 좌표 찾기
    for p in range(len(park)):
        if 'S' in park[p]:
            start = [p, park[p].find('S')]
            
    x, y = start    
    for route in routes:
        d, n = route.split(' ')
        n = int(n)
        if d == 'E':
            ny = y + n
            if ny >= w :
                continue
            if 'X' in park[x][y:ny+1] :
                continue
            y = ny
            
        elif d == 'W':
            ny = y - n
            if ny < 0:
                continue
            if 'X' in park[x][ny:y+1]:
                continue
            y = ny
            
        elif d == 'S' :
            nx = x + n
            if nx >= h :
                continue
            if 'X' in [x[y] for x in park[x:nx+1]]:
                continue
            x = nx
        else :
            nx = x - n
            if nx < 0:
                continue
            if 'X' in [x[y] for x in park[nx:x+1]]:
                continue
            x = nx

    answer = [x, y]
    return answer
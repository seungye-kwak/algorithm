from collections import deque
def solution(players, m, k):
    # 같은 시간대에 게임을 이용하는 사람이 m명 늘어날 때마다 서버 1대가 추가로 필요함
    # 어느 시간대의 이용자가 m명 미만이라면 서버 증설 필요하지 않음
    # 어느 시간대의 이용자가 n*m명 이상 (n+1) * m 명 미만이라면 최소 n대의 증설된 서버가 운영 중이어야함
    # 한 번 증설한 서버는 k시간동안 운영하고 그 이후에는 반납
    server = 0
    server_time = deque([])
    answer = 0
    for t in range(24) :
        # 현재 플레이어 수
        now_players = players[t]
        n = now_players//m
        
        if server_time and server_time[0][2] < t :
            del_server = server_time.popleft()[0]
            server -= del_server
        
        if server < n :
            plus = n-server
            server += plus
            answer += plus
            server_time.append((plus, t, t+k-1))
        
    return answer
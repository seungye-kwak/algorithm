def solution(schedules, timelogs, startday):
    answer = 0
    
    # 멤버별 허용 출근 시간
    members_time = []
    for s in schedules:
        q, r = s // 100, s % 100
        if r >= 50 :
            q, r = q+1, r + 10 - 60
        else :
            q, r = q, r + 10
        members_time.append(q*100 + r)
    
    # 멤버별 실제 출근 시간
    for i in range(len(timelogs)):
        attend = 0
        limit = members_time[i]
        for t, time in enumerate(timelogs[i]):
            if (startday + t)%7 in (6, 0):
                continue
            
            if time <= limit :
                attend += 1
        
        if attend == 5 :
            answer += 1
            
    return answer
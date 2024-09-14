def solution(video_len, pos, op_start, op_end, commands):
    video_len_mm, video_len_ss = int(video_len.split(':')[0]), int(video_len.split(':')[1])
    pos_mm, pos_ss = int(pos.split(':')[0]), int(pos.split(':')[1])
    op_start_mm, op_start_ss = int(op_start.split(':')[0]), int(op_start.split(':')[1])
    op_end_mm, op_end_ss = int(op_end.split(':')[0]), int(op_end.split(':')[1])
    
    # 오프닝 건너뛰기
    def skip_opening(pos_mm, pos_ss) :
        if pos_mm<op_start_mm or pos_mm > op_end_mm :
            pass
        elif pos_mm == op_start_mm and pos_ss < op_start_ss :
            pass
        elif pos_mm == op_end_mm and pos_ss > op_end_ss :
            pass
        else :
            pos_mm, pos_ss = op_end_mm, op_end_ss
        return pos_mm, pos_ss
            
    # next, prev
    def video_function(command, pos_mm, pos_ss) :
        if command == 'next' :
            # 10초 이동
            pos_ss += 10
            
            if pos_ss >= 60 :
                pos_mm += 1
                pos_ss -= 60
                
            if pos_mm > video_len_mm or (pos_mm == video_len_mm and pos_ss > video_len_ss) :
                # 전체 비디오 길이 넘어가면 비디오 마지막 지점으로
                pos_mm, pos_ss = video_len_mm, video_len_ss
        else :
            # 10초 전으로 이동
            pos_ss -= 10
            
            if pos_ss < 0 :
                pos_mm -= 1
                pos_ss += 60
                
            if pos_mm < 0 :
                pos_mm, pos_ss = 0, 0
        return pos_mm, pos_ss
                
    # 시작 pos가 오프닝 지점에 있는지 확인
    pos_mm, pos_ss = skip_opening(pos_mm, pos_ss)
    
    for c in commands :
        pos_mm, pos_ss = video_function(c, pos_mm, pos_ss)
        pos_mm, pos_ss = skip_opening(pos_mm, pos_ss)
        
    str_pos_mm, str_pos_ss = str(pos_mm), str(pos_ss)
    
    answer = ''
    for s in [str_pos_mm, ':',str_pos_ss] :
        if s == ':' :
            answer += s
        elif len(s) == 1:
            answer += '0'+s
        else :
            answer += s
    return answer
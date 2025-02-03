def solution(cap, n, deliveries, pickups):
    answer = 0

    # 뒤에서부터 배달과 수거를 진행
    d_remain, p_remain = 0, 0  # 배달 및 수거할 잔여 박스
    
    for i in range(n - 1, -1, -1):  # 가장 먼 위치부터 체크
        d_remain += deliveries[i]  # 해당 위치에서 배달할 박스 추가
        p_remain += pickups[i]  # 해당 위치에서 수거할 박스 추가
        
        # 배달과 수거를 한번에 처리하기 위해 필요한 이동 횟수 계산
        move_count = max((d_remain + cap - 1) // cap, (p_remain + cap - 1) // cap)
        
        if move_count > 0:
            answer += (i + 1) * 2 * move_count  # 왕복 거리 추가
            d_remain -= move_count * cap  # 배달된 박스 차감
            p_remain -= move_count * cap  # 수거된 박스 차감

    return answer
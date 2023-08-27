def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost) # 이 부분을 set(reserve) 
    lost_set = set(lost) - set(reserve) # 이 부분을 set(lost)로 했을 때는 실패

		# 자료형의 문제는 아닌 것 같고 중복되지 않는다는 조건을 코드로 구현해야 하는 듯
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
            
    answer = n - len(lost_set)
    
    return answer
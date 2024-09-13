def solution(diffs, times, limit):
    def calculate_time(level):
        time = 0
        for i in range(len(diffs)) :
            if level >= diffs[i] :
                time += times[i]
            else :
                time += (diffs[i]-level)*(times[i-1]+times[i]) + times[i]
            
            if time > limit :
                break
        return time <= limit
    
    answer = 1
    start = 1
    end = max(diffs)
    
    while start <= end :
        mid = (start + end) // 2
        
        if calculate_time(mid) :
            answer = mid
            end = mid - 1
        else : 
            start = mid + 1

    return answer
        
from collections import deque

def end_time(start_time, time):
    h,m = start_time.split(':')
    if int(m) + int(time) >= 60:
        if int(m) + int(time) >= 120:
            h = int(h)+2
            m = int(m) + int(time)-120
        else :
            h = int(h)+1
            m = int(m)+int(time)-60
    else :
        h = int(h)
        m = int(m) + int(time)
    return f'{h}:{m}'

def hour_to_minute(str_time):
    h, m = str_time.split(':')
    total = int(h)*60+int(m)
    return total

def solution(plans):
    plans.sort(key=lambda x: x[1]) # 일찍 시작하는 순으로 정렬
    stack_= deque([])
    answer = []
    for p in range(len(plans)) :
        if p == len(plans)-1:
            # 마지막 과제일 경우
            answer.append(plans[p][0])
            break
        start = hour_to_minute(plans[p][1])
        end = hour_to_minute(end_time(plans[p][1], plans[p][2]))
        next_start = hour_to_minute(plans[p+1][1])
        if end <= next_start :
            # 해당 과제의 끝나는 시간이 다음 과제의 시작 시간보다 작거나 같으면
            answer.append(plans[p][0]) # 해당 과제 마무리
            while stack_ :
                # stack_에 과제가 있다면
                subject = stack_.pop()
                if end+subject[2] <= next_start:
                    print(end, next_start)
                    answer.append(subject[0])
                    end = end+subject[2]
                else :
                    subject[2] = subject[2] - (next_start - end)
                    stack_.append(subject)
                    break
        else :
            plans[p][2] = int(plans[p][2]) - (next_start-start) # 남은 과제 시간
            stack_.append(plans[p])
            
    while stack_ :
        answer.append(stack_.pop()[0])
    return answer
def solution(n):
    # 가로가 홀수일 때는 바닥 가득 채우기 불가능
    if n%2==1 :
        return 0
    answer = [0, 3, 11]
    idx = n//2
    if idx<3:
        return answer[idx]
    
    for i in range(3, idx+1):
        answer.append((answer[i-1]*answer[1]+
                      sum(answer[1:i-1])*2+2)%1000000007)
    return answer[idx]
    
def solution(storey):
    answer = 0

    while storey > 0:
        remainder = storey % 10
        next_digit = (storey // 10) % 10  # 다음 자리 숫자 확인

        if remainder < 5:
            answer += remainder
        elif remainder > 5:
            answer += (10 - remainder)
            storey += 10  # 반올림 효과 적용
        else:  # remainder == 5일 때
            if next_digit >= 5:
                answer += (10 - remainder)
                storey += 10
            else:
                answer += remainder
        
        storey //= 10  # 한 자리 줄이기

    return answer
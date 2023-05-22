n, m = map(int, input().split())

# 기존 코드에서 1 따로 처리해준 경우

def sick_night(n, m):
    # n:세로, m:가로
    # 이동횟수가 >= 4인 경우 모든 방법 다 한 번씩 사용해야 함
    if n == 1 :
        total = 1
        
    elif n < 3:
        # 위아래 2칸 이동 불가능, 오직 위아래 1칸과 오른쪽2칸만 가능
        if m <= 6:
            # 가로가 7 이하인 경우 시작칸 제외하고 //2(2칸 이동)
            total = (m - 1) // 2 + 1
        else:
            total = 4  # 위아래 2칸 이동할 수 없기 때문에 최대 4칸까지 가능

    else:
        # 세로가 3보다 크거나 같은 경우 중
        if m >= 7 :
            # 가로길이가 7보다 크면 모든 이동방법 다 사용 후 남은 가로길이만큼 이동 가능
            total = (m-7) + 5
        elif m > 4 :
            total = 4
        else :
            total = m
            
    return total


print(sick_night(n, m))
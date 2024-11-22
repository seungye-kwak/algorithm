from collections import Counter
def solution(k, tangerine):
    # 서로 다른 종류의 수를 최소화
    # k개만 담을 수 있음
    # 서로 다른 종류의 수 최솟값 return
    answer = 0
    tang_d = Counter(tangerine)
    tang_d = sorted(tang_d.items(), key=lambda item: -item[1])
    box = 0
    for t, num in tang_d:
        if box >= k:
            break
        box += num
        answer += 1
    return answer
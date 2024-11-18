from collections import Counter
def solution(weights):
    answer = 0
    weight_count = Counter(weights)  # 각 무게의 빈도를 카운트
    for w in sorted(weight_count.keys()):  # 무게 순으로 정렬 후 탐색
        # 조건을 만족하는 경우들을 각각 체크하고 해당 조합 수를 카운트
        answer += weight_count[w] * (weight_count[w] - 1) // 2  # 같은 무게인 경우의 조합 수
        for ratio in [3/2, 4/2, 4/3]:  # 특정 조건을 만족하는 조합 탐색
            target = w * ratio
            if target in weight_count:
                answer += weight_count[w] * weight_count[target]

    return answer
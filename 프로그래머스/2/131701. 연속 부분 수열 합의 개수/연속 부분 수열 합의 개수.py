def solution(elements):
    n = len(elements)
    elements_extended = elements * 2  # 원형 처리를 위한 확장
    unique_sums = set()
    
    # 길이 1부터 n까지 가능한 모든 부분 수열 합 계산
    for length in range(1, n + 1):
        for start in range(n):  # 원래 배열 길이만큼만 시작 위치 선택
            sub_sum = sum(elements_extended[start:start + length])
            unique_sums.add(sub_sum)
    
    return len(unique_sums)
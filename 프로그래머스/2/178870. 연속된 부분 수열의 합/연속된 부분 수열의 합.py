def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0
    current_sum = 0
    answer = [-1, -1]
    min_length = float('inf')  # 최소 길이를 추적

    while right < n:
        current_sum += sequence[right]  # 오른쪽 포인터의 값을 더함

        # current_sum이 k와 같거나 더 클 때까지 왼쪽 포인터를 이동하며 최소 길이를 찾음
        while current_sum >= k:
            if current_sum == k:
                if right - left < min_length:  # 더 짧은 길이의 부분수열을 찾으면 갱신
                    min_length = right - left
                    answer = [left, right]
            current_sum -= sequence[left]
            left += 1
        
        right += 1
    
    return answer
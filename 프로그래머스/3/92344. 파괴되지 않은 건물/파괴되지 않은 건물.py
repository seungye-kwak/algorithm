def solution(board, skill):
    # 1. 누적합 배열 초기화
    n, m = len(board), len(board[0])
    effect = [[0] * (m + 1) for _ in range(n + 1)]

    # 2. 스킬 효과 기록
    for type_, r1, c1, r2, c2, degree in skill:
        if type_ == 1:  # 공격
            degree = -degree
        # 누적합 기록
        effect[r1][c1] += degree
        effect[r1][c2 + 1] -= degree
        effect[r2 + 1][c1] -= degree
        effect[r2 + 1][c2 + 1] += degree

    # 3. 행별 누적합 계산
    for i in range(n):
        for j in range(1, m):
            effect[i][j] += effect[i][j - 1]

    # 4. 열별 누적합 계산
    for j in range(m):
        for i in range(1, n):
            effect[i][j] += effect[i - 1][j]

    # 5. 원본 board에 누적합 적용 및 양수 셀 개수 계산
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += effect[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

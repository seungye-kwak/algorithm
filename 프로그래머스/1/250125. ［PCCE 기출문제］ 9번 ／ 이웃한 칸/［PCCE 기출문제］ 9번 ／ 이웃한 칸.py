def solution(board, h, w):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    max_x = len(board)
    max_y = len(board[0])
    
    answer = 0
    for i in range(4) :
        nx = h + dx[i]
        ny = w + dy[i]
        if nx < 0 or nx >=max_x or ny < 0 or ny >= max_y :
            continue
            
        if board[nx][ny] == board[h][w]:
            answer += 1
            
    return answer
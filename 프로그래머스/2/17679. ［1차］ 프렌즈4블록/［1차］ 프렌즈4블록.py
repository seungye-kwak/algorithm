def solution(m, n, board):
    answer = 0
    # board의 문자열을 lst 형태로 변환
    board = [list(x) for x in board]
    
    delete = set()
    while True :
        for i in range(m-1) :
            for j in range(n-1) :
                t = board[i][j]
                if t == [] :
                    # 없어진 값일 경우
                    continue
                else :
                    if t == board[i][j+1] and t == board[i+1][j] and t == board[i+1][j+1]:
                        delete.add((i,j))
                        delete.add((i,j+1))
                        delete.add((i+1,j))
                        delete.add((i+1,j+1))
        if delete :
            answer += len(delete)
            for i, j in delete :
                # 삭제
                board[i][j] = []
            delete = set() # 1턴 끝나면 다시 리셋
        else :
            break
            
        # 블록 이동 (아래로만 이동됨)
        while True :
            move = 0
            for i in range(m-1) :
                for j in range(n) :
                    if board[i][j] != [] and board[i+1][j] == [] :
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        move = 1
            if move == 0 :
                break
    return answer
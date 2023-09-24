from itertools import combinations_with_replacement 
def solution(n, info):
    answer = [-1]
    result_list = []
    score_num = [0,1,2,3,4,5,6,7,8,9,10]
    mx_board = [-1]
    mx_gap = -1
    for score_list in list(combinations_with_replacement(score_num, n)):
        lion = 0
        appeach = 0
        
        score_board = [0 for _ in range(11)]
        for score in score_list:
            score_board[10 - score] += 1
            
        for i in range(11):
            if score_board[i] == 0 and info[i] == 0:
                continue
            if score_board[i] > info[i]:
                lion += (10 - i)
            else:
                appeach += (10 - i)
                
        if lion > appeach:
            gap = lion - appeach
            if gap > mx_gap:
                mx_gap = gap
                mx_board = score_board
        
    return mx_board
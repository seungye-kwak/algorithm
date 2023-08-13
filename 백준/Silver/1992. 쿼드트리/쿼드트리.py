import sys

n = int(input())
paper = [[] for _ in range(n)]
for i in range(n) :
    paper[i] = [int(x) for x in input()]
    
result = []
def solution(x, y, n) :
    color = paper[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if color != paper[i][j] :
                result.append('(')
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                result.append(')')
                return 
    if color == 0:
        result.append('0')
    else :
        result.append('1')
        
solution(0, 0, n)
print(''.join(result))
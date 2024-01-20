import sys
input = sys.stdin.readline

n = int(input())

error=0
stack = []
answer = []
num = 1
for _ in range(n) :
    k = int(input())
    
    while num <= k :
        stack.append(num)
        num += 1
        answer.append('+')
        
    if stack[-1] == k :
        stack.pop()
        answer.append('-')
    
    else :
        print('NO')
        error = 1
        break
    
if error == 0 :
    print(*answer, sep='\n')
import sys

sent = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())
n = len(sent)

stack = []
for _ in range(m) :
    command = list(sys.stdin.readline().split()) # L, D, B, P
    
    if command[0] == 'L' :
        if sent :
            stack.append(sent.pop())
    
    elif command[0] == 'D' :
        if stack :
            sent.append(stack.pop())
            
    elif command[0] == 'B' :
        if sent :
            sent.pop()
        
    elif command[0] == 'P' :
        sent.append(command[1])
        
sent.extend(reversed(stack))
print(''.join(sent))
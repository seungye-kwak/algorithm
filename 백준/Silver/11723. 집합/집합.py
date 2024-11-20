import sys
input = sys.stdin.readline

M = int(input()) # 연산의 수
S = set()
for _ in range(M):
    command = input().split()
    if len(command) > 1:
        command, num = command[0], int(command[1])
    else:
        command = command[0]
        
    if command == 'add':
        S.add(num)
    elif command == 'remove':
        S.discard(num)
    elif command == 'check':
        print(1 if num in S else 0)
    elif command == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif command == 'all':
        S = set(range(1,21))
    elif command == 'empty':
        S.clear()
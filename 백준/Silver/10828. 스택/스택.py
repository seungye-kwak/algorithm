import sys
input = sys.stdin.readline
n = int(input()) # 명령 수

stack_ = []
for _ in range(n) :
    msg = list(map(str, input().split()))
    if msg[0] == 'push' :
        stack_.append(int(msg[1]))
    elif msg[0] == 'pop' :
        if len(stack_)>0:
            print(stack_.pop())
        else :
            print(-1)
    elif msg[0] == 'size' :
        print(len(stack_))
    elif msg[0] == 'empty' :
        if len(stack_) > 0 :
            print(0)
        else :
            print(1)
    elif msg[0] == 'top' :
        if len(stack_)>0 :
            print(stack_[-1])
        else :
            print(-1)
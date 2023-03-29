sent = input()

stack = []
sticks=0
for i in range(len(sent)) :
    if sent[i] == '(' :
        if sent[i+1]==')' :
            sticks += len(stack)
        else :
            stack.append('(')
    else :
        if sent[i-1] != '(' :
            stack.pop()
            sticks += 1
            
print(sticks)        
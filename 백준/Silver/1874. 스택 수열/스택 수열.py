n = int(input())

stack=[]
pm = []
num = 1
stop = 0
for i in range(n) :
    a = int(input())
    while num <= a :
        stack.append(num)
        num+=1
        pm.append('+')
    
    if stack[-1] == a :
        stack.pop()
        pm.append('-')
    else :
        print('NO')
        stop=1
        break
        
if stop == 0:
    for i in pm :
        print(i)
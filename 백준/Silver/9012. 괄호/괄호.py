n = int(input())

for _ in range(n) :
    sum_=0
    msg = str(input())
    for i in msg :
        if i == '(' :
            sum_+=1
        elif i == ')' :
            sum_ -= 1
            
        # 앞 괄호가 없는 상황에서 뒷 괄호가 나타난 경우    
        if sum_ < 0 :
            break
            
    if sum_ == 0 :
        print('YES')
    else :
        print('NO')
n = int(input()) # 1<=n<=26
sent = input()

a_lst = []
n_lst = []
for i in sent :
    if (i.isalpha()) & (i not in a_lst) :
        a_lst.append(i)
        n_lst.append(int(input()))
    if len(a_lst) > n :
        break
alpha_dict = dict(zip(a_lst, n_lst))
    
stack = []
for i in sent :
    if i.isalpha() :
        stack.append(alpha_dict[i])
    else :
        a = stack.pop() # 가장 위 영어
        result = stack.pop() # 가장 위-1 영어
            
        if i == '+' :
            result += a
        elif i == '*' :
            result *= a
        elif i == '-' :
            result-= a
        elif i == '/' :
            result/=a
                
        stack.append(result)

print("{:.2f}".format(stack[0]))
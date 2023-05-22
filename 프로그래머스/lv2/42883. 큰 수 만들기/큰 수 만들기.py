def solution(number, k):
    stack_ = []
    for i in number :
        while k > 0 and stack_ and stack_[-1] < i:
            stack_.pop()
            k-=1
        stack_.append(i)
            
    return ''.join(map(str, stack_[:len(number)-(k)]))
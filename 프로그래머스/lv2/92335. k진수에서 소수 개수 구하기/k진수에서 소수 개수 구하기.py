def is_prime_number(x):
    for i in range(2, int(int(x)**0.5)+1) :
        if x%i == 0:
            return False
    return True

def solution(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    rev_base = rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
    lst = rev_base.split('0')
    
    answer=0 # 소수 개수
    for i in lst :
        if i == '' :
            continue
        if int(i) == 1 :
            continue
        if is_prime_number(int(i)) :
            answer+=1
            
    return answer

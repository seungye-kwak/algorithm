def get_max_divisor(n:int)->int:
    if n==1:
        return 0
    
    data=[]
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            data.append(i)
            if n//i<=10000000:
                return n//i
    if len(data)>=1:
        return data[-1]
    return 1

def solution(begin, end):
    answer = []
    
    for i in range(begin,end+1):#O(5000)
        # 약수 중에서 자기 자신을 제외한 최대 약수를 구한다.
        max_divisor=get_max_divisor(i)
        answer.append(max_divisor)
        
    return answer
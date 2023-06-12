import sys
from itertools import combinations
from math import prod
input = sys.stdin.readline

n = int(input())
s_lst=[]
b_lst=[]
for _ in range(n) :
    s, b = map(int, input().split()) # 신맛, 쓴맛
    s_lst.append(s)
    b_lst.append(b)
    

def cook(s_lst, b_lst) :
    answer = 1000000000
    for i in range(1, n+1) :
        for x in range(len(list(combinations(s_lst, i)))) :
            s_comb = list(combinations(s_lst, i))[x]
            b_comb = list(combinations(b_lst, i))[x]
            
            total_s = prod(s_comb)
            total_b = sum(b_comb)
            
            if abs(total_s-total_b) < answer :
                answer = abs(total_s-total_b)
    
    return answer


print(cook(s_lst, b_lst))
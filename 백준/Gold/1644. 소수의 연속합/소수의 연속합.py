import sys
input = sys.stdin.readline

N = int(input())

import math

if N < 2 :
    print(0)
    exit(0)

def is_prime(n) :
    nums = [True] * (n + 1)
    nums[0] = nums[1] = False
    
    limit = int(math.sqrt(n)) + 1
    
    for i in range(2, limit):
        if nums[i] :
            step_from = i * i
            nums[step_from:n+1:i] = [False] * (((n-step_from) // i) + 1)
    return [x for x, v in enumerate(nums) if v]

prime_lst = is_prime(N)

left, right, curr = 0, 0, 0
answer = 0
while True:
    if right < len(prime_lst) and curr < N :
        curr += prime_lst[right]
        right += 1
        
    elif curr == N :
        answer += 1
        curr -= prime_lst[left]
        left += 1
        
    elif left < len(prime_lst):
        curr -= prime_lst[left]
        left += 1
    else :
        break
        
print(answer)

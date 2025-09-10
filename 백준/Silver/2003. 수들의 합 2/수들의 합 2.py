n, m = map(int, input().split())
nums = list(map(int, input().split()))

left, right, curr = 0, 0, 0
answer = 0

while True :
    if curr < m and right < n :
        curr += nums[right]
        right += 1
    elif curr == m :
        answer += 1
        curr -= nums[left]
        left += 1
    elif left < n :
        curr -= nums[left]
        left += 1
    else :
        break
    
print(answer)
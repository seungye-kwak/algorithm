N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right, curr = 0, 0, 0

min_length = float('inf')
while True:
    if curr < S and right < N :
        # 현재 부분합이 S보다 작고 오른쪽 포인터가 범위 내에 있으면
        curr += nums[right] # 현재 값에 오른쪽 포인트 값을 더하고
        right += 1 # 오른쪽 포인트를 한 칸 이동
    
    elif curr >= S:
        # 현재 부분합이 S보다 크거나 같으면
        curr_length = right - left
        min_length = min(min_length, curr_length)
        curr -= nums[left]
        left += 1
        
    else :
        break
    
if min_length == float('inf'):
    print(0)
else :
    print(min_length)
h, w = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0
for i in range(1, len(blocks)-1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])

    min_height = min(left_max, right_max)
    
    answer += max(0, min_height-blocks[i])
print(answer)
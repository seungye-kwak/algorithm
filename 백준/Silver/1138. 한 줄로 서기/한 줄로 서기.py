n = int(input()) # 줄 서는 사람 수
# 키가 1인 사람부터 차례대로 자기보다 키 큰 사람이 왼쪽에 몇 명 있는지 수
lst = list(map(int, input().split())) 

line = []
line.append(n)
for i in reversed(range(n-1)) :
    if lst[i] < len(line) :
        line = line[:lst[i]] + [i+1] + line[lst[i]:]
    else : 
        line.append(i+1)
        
print(*line)
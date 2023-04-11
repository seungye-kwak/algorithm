import sys
input = sys.stdin.readline

n = int(input())
def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return 
    
    hanoi_tower(n-1, start, 6-start-end)
    print(start, end) # n번째 원판을 end에 올림
    hanoi_tower(n-1, 6-start-end, end) # 가운데 있는 원판들을 end 에 올림
    
print(2**n-1)
if n <= 20 :
    hanoi_tower(n, 1, 3)
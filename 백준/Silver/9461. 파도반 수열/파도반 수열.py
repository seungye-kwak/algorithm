import sys
input = sys.stdin.readline

t = int(input())

cache = [0] * 101
cache[1] = 1
cache[2] = 1
cache[3] = 1

for i in range(4, 101) :
    cache[i] = cache[i-2] + cache[i-3]
    
for _ in range(t) :
    num = int(input())
    print(cache[num])
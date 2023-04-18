n = int(input())
cache = [0]*1000001
for i in range(2, 1000001) :
    cache[i] = cache[i-1] + 1
    if i%2 == 0 :
        cache[i] = min(cache[i], cache[i//2]+1)
    if i%3 == 0 :
        cache[i] = min(cache[i], cache[i//3]+1)
        
print(cache[n])
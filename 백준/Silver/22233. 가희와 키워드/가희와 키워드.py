import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

keywords = dict()
cnt = 0
for _ in range(n):
    keywords[input().rstrip()] = 1
    cnt +=1
    
for _ in range(m):
    use = input().rstrip().split(',')
    for w in use:
        if keywords.get(w):
            cnt -= 1
            del keywords[w]
    print(cnt)
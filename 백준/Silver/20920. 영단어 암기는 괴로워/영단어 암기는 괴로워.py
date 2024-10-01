import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

word_dict = {}
for _ in range(n) :
    word = input().rstrip()
    if len(word) >= m:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else :
            word_dict[word] += 1
            
result = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for r in result :
    print(r[0])
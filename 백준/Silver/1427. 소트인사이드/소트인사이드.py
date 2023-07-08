import sys
input = sys.stdin.readline

n = input().strip()

lst = [x for x in n]
lst.sort(reverse=True)
print(''.join(lst))
import sys

input = sys.stdin.readline
n = int(input().strip())
colors = input().strip()

cnt = []

rr = colors.rstrip('R')
cnt.append(rr.count('R'))

br = colors.rstrip('B')
cnt.append(br.count('B'))

rl = colors.lstrip('R')
cnt.append(rl.count('R'))

bl = colors.lstrip('B')
cnt.append(bl.count('B'))

print(min(cnt))
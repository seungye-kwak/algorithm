import re

N = int(input())
lst = []
for _ in range(N):
    serials = input()
    nums = sum([int(x) for x in re.sub(r'[^0-9]', '', serials)])
    lst.append((serials, len(serials), nums))
    
for i in sorted(lst, key=lambda x: (x[1], x[2], x[0])):
    print(i[0])
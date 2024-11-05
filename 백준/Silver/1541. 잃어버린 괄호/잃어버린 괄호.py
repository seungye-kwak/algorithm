cal = input()
cals = cal.split('-')

cals2 = []
for c in cals:
    if '+' in c:
        cs = c.split('+')
        num = sum([int(x) for x in cs])
    else:
        num = int(c)
    cals2.append(num)
    
answer = cals2[0]
for i in range(1, len(cals2)):
    answer -= cals2[i]
print(answer)
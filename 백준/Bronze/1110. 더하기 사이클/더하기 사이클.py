n = int(input())
new = n
cnt = 0
while True :
    if new < 10 :
        l = 0
        r = n
        new = new*10+new
        cnt += 1
    else :
        l = new//10
        r = new%10
        new = r*10 + (l+r)%10
        cnt += 1
    if new == n :
        break
print(cnt)
    
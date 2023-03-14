t = int(input())

def prime_tf(num):
    pm = True
    if num == 1:
        pm = False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            pm = False
    return pm

for _ in range(t):
    n = int(input())
    a = n // 2
    b = n // 2
    while a > 1:
        if (prime_tf(a) == True) & (prime_tf(b) == True):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
m, n = map(int, input().split())

def gcd(a, b) :
    while b > 0 :
        a, b = b, a%b
    return a

print(int(gcd(m,n)))
print(int(m*n/gcd(m,n)))
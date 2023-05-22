import sys
input = sys.stdin.readline

def max_price(n, price):
    max_p = 0
    rev=0
    for i in range(len(price)-1, -1, -1) :
        if price[i] > max_p :
            max_p = price[i]
        else :
            rev += max_p - price[i]
    return rev

T = int(input())

while True:
    if T == 0:
        break
    n = int(input())
    price = list(map(int, input().split()))

    print(max_price(n, price))

    T -= 1
import sys
input = sys.stdin.readline

n = int(input())
def fibo(num) :
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)

print(fibo(n))
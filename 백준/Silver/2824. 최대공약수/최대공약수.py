from functools import reduce

n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

# n개의 수를 모두 곱하면 A, m개의 수를 모두 곱하면 B
# 최대공약수 구하는 프로그램 작성

a = reduce(lambda x, y: x * y, n_lst)
b = reduce(lambda x, y: x * y, m_lst)


# 최대공약수 구하는 함수
def gcd(a, b):
    if a >= b:
        while b > 0:
            a, b = b, a % b
        return a
    else:
        while a > 0:
            b, a = a, b % a
        return b


gcd_num = gcd(a, b)

if len(str(gcd_num)) > 9:
    gcd_num = str(gcd_num)[-9:]
else:
    gcd_num = str(gcd_num)

print(gcd_num)

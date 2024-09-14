number = int(input())

answer = 0

while number // 100 != 0 or number%100 != 0:
    answer += number % 100
    number //= 100

print(answer)
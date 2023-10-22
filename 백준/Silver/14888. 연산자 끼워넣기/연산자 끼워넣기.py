from itertools import permutations
n = int(input())
number = list(map(int, input().split()))
op = list(map(int, input().split()));
operator = '+' * op[0] + '-' * op[1] + '*' * op[2] + '/' * op[3]
operator_perm = permutations(operator, n-1)

max_result = - int(1e9)
min_result = int(1e9)
for perm in operator_perm:
    result = number[0]
    for i in range(1, n):
        if perm[i-1] == '+':
            result += number[i]
        elif perm[i-1] == '-':
            result -= number[i]
        elif perm[i-1] == '*':
            result *= number[i]
        elif perm[i-1] == '/':
            if result < 0 and number[i] > 0: 
                result = -1*( result*(-1) // number[i])
            else:
                result //= number[i]
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)
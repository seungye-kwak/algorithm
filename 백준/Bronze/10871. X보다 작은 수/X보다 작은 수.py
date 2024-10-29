n, x = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = [a for a in lst if a < x]

print(*lst2)
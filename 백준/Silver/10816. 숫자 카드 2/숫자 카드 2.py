N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
what = list(map(int, input().split()))

def binary(n, card, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if n == card[m]:
        return card[start : end + 1].count(n)
    elif n < card[m]:
        return binary(n, card, start, m - 1)
    else:
        return binary(n, card, m + 1, end)


n_dic = {}
for n in card:
    start = 0
    end = N - 1
    if n not in n_dic:
        n_dic[n] = binary(n, card, start, end)

print(" ".join(str(n_dic[x]) if x in n_dic else "0" for x in what))
from collections import Counter

word = input()
counts = Counter(word.upper())
max_str = [k for k, v in counts.items() if v == counts.most_common()[0][1]]

answer = '?' if len(max_str) > 1 else max_str[0]
print(answer)
import sys

input = sys.stdin.readline

n = int(input().strip())
used = set()  # 이미 사용한 단축키(소문자)

def wrap_at(s, idx):
    return s[:idx] + '[' + s[idx] + ']' + s[idx+1:]

out = []
for _ in range(n):
    s = input().rstrip('\n')
    idx = -1

    # 1단계: 각 단어의 첫 글자 (왼→오)
    parts = s.split(' ')  # 문제 조건상 단어는 공백 하나로 구분
    pos = 0  # 현재 단어의 첫 글자가 원문에서 시작되는 인덱스
    for w in parts:
        if w:  # 방어적
            c = w[0]
            if c.isalpha() and c.lower() not in used:
                idx = pos
                break
        # 다음 단어의 시작 위치 = 현재 단어 길이 + 공백 1
        pos += len(w) + 1

    # 2단계: 문자열 전체 스캔
    if idx == -1:
        for i, ch in enumerate(s):
            if ch.isalpha() and ch.lower() not in used:
                idx = i
                break

    if idx == -1:
        out.append(s)
    else:
        used.add(s[idx].lower())
        out.append(wrap_at(s, idx))

print('\n'.join(out))
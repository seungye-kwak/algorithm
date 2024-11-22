import sys
input = sys.stdin.readline

# 팀의 역량의 최소값을 최대화하기 위한 팀 구성
n = int(input())
members = sorted(list(map(int, input().split())), reverse=True)

mid = n
teams = []
while mid < 2*n:
    # print(mid, (2*n-1)-mid)
    teams.append(sum([members[mid], members[(2*n-1)-mid]])) # (2,1), (3,0)
    mid += 1
print(min(teams))
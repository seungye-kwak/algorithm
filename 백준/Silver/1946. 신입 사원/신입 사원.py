import sys
input = sys.stdin.readline

T = int(input())  # 테스트케이스 수

def hired(n, p_lst):
    p_lst = sorted(p_lst, key=lambda x: x[0])
    view_cut = p_lst[0][1]  # 초기값 : 서류 1등의 면접 점수
    join = 1  # 서류 1등은 입사 확정
    for grade in p_lst[1:]:
        if grade[1] < view_cut:
            # 직전 입사자의 면접점수 등수보다 낮으면
            join += 1  # 입사 확정
            view_cut = grade[1]  # 면접 커트라인보다 낮으면
    return join


while T:
    n = int(input())
    p_lst = []
    for _ in range(n):
        a, b = map(int, input().split())
        p_lst.append([a, b])

    print(hired(n, p_lst))
    T -= 1
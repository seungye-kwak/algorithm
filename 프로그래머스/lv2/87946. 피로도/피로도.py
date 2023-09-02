from itertools import permutations

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    for p in permutations(dungeons, n) :
        cnt = 0
        hp = k
        for permu in p :
            if permu[0] <= hp :
                # 현재 내 피로도가 최소필요도보다 같거나 높으면
                hp -= permu[1] # 현재 피로도에서 소모 피로도 빼기
                cnt += 1
            else :
                break
        if cnt > answer: 
            answer = cnt
    return answer
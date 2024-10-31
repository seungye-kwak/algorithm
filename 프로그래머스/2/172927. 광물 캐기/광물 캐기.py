# 더이상 사용할 수 있는 곡괭이가 없을 때까지 광물을 캠
def solution(picks, minerals):
    # 각 구간별 피로도 계산
    section_cnt = min(sum(picks), len(minerals)//5 if len(minerals)%5 ==0 else len(minerals)//5+1)
    section_fatigue = [[] for _ in range(section_cnt)]
    start = 0
    for i in range(len(section_fatigue)):
        if start >= len(minerals):
            break
        section = minerals[start:start+5]
        dia, ir, st = 0, 0, 0
        for m in section:
            if m == 'diamond':
                dia += 1
                ir += 5
                st += 25
            elif m == 'iron':
                dia += 1
                ir += 1
                st += 5
            else:
                dia += 1
                ir += 1
                st += 1
            section_fatigue[i] = [dia, ir, st]
        start += 5
    
    section_fatigue.sort(key=lambda x: (-x[2], -x[1], -x[0]))
    
    final_fatigue = 0
    for fatigue in section_fatigue:
        if picks[0] > 0:
            final_fatigue += fatigue[0]
            picks[0] -= 1
        elif picks[1] > 0 :
            final_fatigue += fatigue[1]
            picks[1] -= 1
        elif picks[2] > 0:
            final_fatigue += fatigue[2]
            picks[2] -= 1
            
    return final_fatigue

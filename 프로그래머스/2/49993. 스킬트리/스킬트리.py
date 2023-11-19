def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        s = ''
        for sk in st :
            if sk in skill:
                s += sk
                
        if skill[:len(s)] == s:
            answer += 1
            
    return answer
def open_box(start, lst, g) :
    group = g.copy()
    group.append(start)
    idx = start-1
    while True :
        if lst[idx] not in group :
            group.append(lst[idx])
            idx = lst[idx]-1
        else :
            break

    return group

def solution(cards) :
    answer = 0
    for i in cards :
        g1 = open_box(i, cards, [])
        if len(g1) == len(cards) :
            pass

        max_g2 = 0
        for x in [a for a in cards if a not in g1] :
            g2 = open_box(x, cards, g1)
            g2 = [k for k in g2 if k not in g1]

            if len(g2) > max_g2 :
                max_g2 = len(g2)
        
        score = len(g1) * max_g2
        if score > answer :
            answer = score

    return answer
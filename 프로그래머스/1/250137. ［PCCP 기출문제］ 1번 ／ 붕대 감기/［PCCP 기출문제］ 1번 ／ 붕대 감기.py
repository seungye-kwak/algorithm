def solution(bandage, health, attacks):
    max_hp = health # 최대 체력
    for a in range(len(attacks)-1) :
        # 공격 받음
        health -= attacks[a][1]
        
        if health <= 0 :
            return -1 
        
        # 다음 공격까지 heal
        heal_time = attacks[a+1][0]-attacks[a][0] - 1
        if heal_time >= bandage[0] :
            health += (bandage[0]*bandage[1] + bandage[2])*(heal_time//bandage[0])
            health += (heal_time%bandage[0])*bandage[1]
        else :
            health += heal_time*bandage[1]
        health = min(max_hp, health) # 최대체력을 넘을 수 없음
        
    # 마지막 공격
    health -= attacks[-1][1]
    
    if health <= 0 :
        return -1
            
    return health
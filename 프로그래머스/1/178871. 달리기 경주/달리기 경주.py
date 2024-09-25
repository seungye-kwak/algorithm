def solution(players, callings):
    # 경주가 끝났을 때 1등부터 순서대로 배열에 담기
    d = {v:k for k, v in enumerate(players)}
    for call in callings:
        idx = d[call]
        d[call] = idx -1
        d[players[idx-1]] = idx
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players
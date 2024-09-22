def solution(array, commands):
    answer = []
    for command in commands :
        a = array[command[0]-1:command[1]]
        aa = sorted(a)[command[-1]-1]
        answer.append(aa)
    return answer
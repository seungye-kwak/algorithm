def collatz(num) :
    result = [num]
    while num != 1 :
        if num%2==0:
            num /= 2
        else :
            num = num*3+1
        result.append(int(num))
    return result

def solution(k, ranges) :
    n = collatz(k)

    answer = []
    for r in ranges:
        area = 0
        new_r = n[r[0]:len(n)+r[1]]

        if r[0] >= len(n)+r[1] :
            answer.append(-1)
            continue

        for i in range(len(new_r)-1) :
            # 사다리꼴 공식 : ((윗변+아랜변)*높이)/2
            area += (((new_r[i]+new_r[i+1])*1)/2)

        answer.append(area)

    return answer
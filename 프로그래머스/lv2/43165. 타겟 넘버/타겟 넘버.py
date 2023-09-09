def solution(numbers, target):
    # 순서를 바꾸지 않아야 함
    # 더하거나 빼기 가능
    start = [0]
    for i in numbers:
        next = []
        for j in start :
            next.append(j+i)
            next.append(j-i)
        start = next
    answer = start.count(target)
    return answer
def solution(info, query):
    # 나올 수 있는 모든 조건
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    # 지원자들이 해당할 수 있는 조건에 점수 넣기
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    # 지원자 점수 오름차순 정렬
    for k in data:
        data[k].sort()

    # 개발자가 원하는 조건에 맞는 인원 수
    answer = list()

    for q in query:
        q = q.split()
        # 개발자가 원하는 조건에 해당하는 사람들의 점수
        scores = data[(q[0], q[2], q[4], q[6])]
        # 개발자가 원하는 점수보다 높은 사람 수 세기
        wanted = int(q[7])
        l,r = 0, len(scores)
        while l < r:
            middle = (l + r)//2
            if scores[middle] >= wanted:
                r = middle
            else:
                l = middle + 1
        answer.append(len(scores)-l)
        
    return answer

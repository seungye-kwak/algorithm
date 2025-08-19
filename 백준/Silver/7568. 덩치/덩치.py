n = int(input())
people = [] 
for _ in range(n) :
    people.append(list(map(int, input().split())))
    
for i in range(n) : 
    rank = 1
    for j in range(n) :
        if i != j :
            if people[i][0] < people[j][0] and people[i][1] < people[j][1] :
                rank += 1
    print(rank, end = ' ')
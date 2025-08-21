n, new, p = map(int, input().split())

if n == 0 :
    print(1)

else :
    scores = list(map(int, input().split()))
    if n == p and scores[-1] >= new :
        print(-1)
        
    else :

        rank = 1
        for i in range(n) :
            if scores[i] > new :
                rank += 1
            else :
                break
        print(rank)
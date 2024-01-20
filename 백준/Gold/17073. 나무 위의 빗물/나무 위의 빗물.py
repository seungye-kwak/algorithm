import sys
input=sys.stdin.readline

N,W=map(int,input().split())
Tree=[ [] for _ in range(N+1) ]

for i in range(N-1):
    a,b=map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)

count=0
for i in range(2,len(Tree)):
    if len(Tree[i])==1: #리프 노드라면
        count+=1

print("%.3f"%(W/count))
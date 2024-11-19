n=int(input())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
s=0
for i in range(n):
    s=sum(mat[i])
    for j in range(n):
        s+=mat[j][i]
    print(s,end=' ')

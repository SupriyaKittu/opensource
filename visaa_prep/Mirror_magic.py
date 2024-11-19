n=int(input())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(n):
    for j in range(n-1,-1,-1):
        print(mat[i][j],end=' ')
    print()

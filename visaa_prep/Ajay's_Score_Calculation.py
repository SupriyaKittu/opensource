N=int(input())
arr=[]
for i in range(N):
    X,Y=map(int,input().split())
    m=X//10
    marks=m*Y
    arr.append(marks)
for i in arr:
    print(i)

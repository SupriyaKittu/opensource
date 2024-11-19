n,m=map(int,input().split())
arr=list(map(int,input().split()))
n1,n2=0,0
for i in arr:
    if i%m==0:
        n1+=i
    else:
        n2+=i
print(n1-n2)

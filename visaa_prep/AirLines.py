x,n=map(int,input().split())
passengers=x*100
if n>passengers:
    r=n-passengers
    if r%100==0:
        planes=r//100
    else:
        planes=(r//100)+1
else:
    planes=0
print(planes)

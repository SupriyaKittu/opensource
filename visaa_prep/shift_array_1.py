n=int(input())
arr=list(map(int,input().split()))
k=arr[0]
for i in range(n):
    if i==n-1:
        arr[n-1]=k
    else:
        arr[i]=arr[i+1]
print(*arr)

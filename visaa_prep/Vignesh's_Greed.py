n=int(input())
arr=list(map(int,input().split()))
max_p=0
p=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]>arr[k] and arr[j]+arr[k]>arr[i] and arr[i]+arr[k]>arr[j]:
                p=arr[i]+arr[j]+arr[k]
                max_p=max(p,max_p)
print(max_p if max_p>0 else -1)

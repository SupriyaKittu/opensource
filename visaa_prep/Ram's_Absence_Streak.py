n=int(input())
arr=list(map(int,input().split()))
max_count=0
count=0
for i in range(n):
    if arr[i]==0:
        count+=1
    else:
        max_count=max(max_count,count)
        count=0
print(max_count)

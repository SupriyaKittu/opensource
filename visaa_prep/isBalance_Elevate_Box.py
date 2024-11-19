n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    left=sum(arr[0:i])
    right=sum(arr[i+1:])
    diff=abs(left-right)
    print(diff,end=' ')

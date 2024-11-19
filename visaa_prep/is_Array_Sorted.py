n=int(input())
arr=list(map(int,input().split()))
a=sorted(arr)
if arr==a:
    print("true")
else:
    print("false")

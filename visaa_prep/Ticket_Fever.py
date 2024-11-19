n=int(input())
for i in range(n):
    n,m=map(int,input().split())
    print(n-m if n>m else 0)

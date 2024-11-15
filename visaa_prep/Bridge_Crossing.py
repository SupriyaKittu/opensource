# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y,z=map(int,input().split())
sum=y
count=0
while(sum+x<=z):
    sum+=x
    count+=1
print(count)

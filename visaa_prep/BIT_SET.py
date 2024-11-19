N=int(input())
k=int(input())
binary=str(0*k)+bin(N)[2:]
if len(binary)>=k and binary[-k]=='1':
    print("true")
else:
    print("false")

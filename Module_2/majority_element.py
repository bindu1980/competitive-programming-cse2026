n=int(input())
arr=list(map(int,input().split()))
b={}
for num in arr:
    if num in b:
        b[num]+=1
    else:
        b[num]=1
high=max(b,key=b.get)
if b[high] > n // 2:
    print(high)
else:
    print(-1)   
    

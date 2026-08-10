n=int(input())
arr= list(map(int,input().split()))
m=int(input())
ar=list(map(int,input().split()))
b=[]
i=0
j=0
while i<n and j<m:
    if arr[i]<ar[j]:
        b.append(arr[i])
        i+=1
    else:
        b.append(ar[j])
        j+=1
while i<n:
    b.append(arr[i])
    i+=1
while j<m:
    b.append(ar[j])
    j+=1
print(*b)

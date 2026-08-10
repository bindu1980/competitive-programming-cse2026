n=int(input())
arr = list(map(int, input().split()))
max_sofar=arr[0]
max_end=0
for i in range(n):
    max_end=max_end+arr[i]
    if max_sofar<max_end:
        max_sofar=max_end
    if max_end<0:
        max_end=0      
print(max_sofar)        

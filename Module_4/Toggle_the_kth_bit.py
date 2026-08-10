def binarydiv(x,y):
    high = x
    low = 0
    while low < high:
        mid = low + (high-low)//2
        if mid*y == x:
            return mid
        elif mid*y > x:
            high = mid -1
        else:
            low = mid +1
x,y = map(int,input().split())
print(binarydiv(x,y))                       
        
     

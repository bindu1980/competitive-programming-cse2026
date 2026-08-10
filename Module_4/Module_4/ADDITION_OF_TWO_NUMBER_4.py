a,b = map(int,input().split())
def add(i,j):
    while j != 0:
        carry = i & j
        i = i ^ j
        j = carry << 1
    return i 
print(add(a,b))       
                

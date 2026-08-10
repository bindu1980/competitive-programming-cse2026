def binary(n):
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res
n = int(input())
k = int(input())
op = binary(n)
op1 = op[::-1]
if op1[k] == '1':
    print(1)
else:
    print(0)        

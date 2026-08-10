# Enter your code here. Read input from STDIN. Print output to STDOUT
def binary(n):
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res

a = int(input())
op1 = binary(a)

count = 0
for i in op1:
    if i == "1":
        count += 1

print(count)

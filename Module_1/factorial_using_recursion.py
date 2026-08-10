# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))

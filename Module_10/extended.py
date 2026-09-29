# Enter your code here. Read input from STDIN. Print output to STDOUT
A, B = map(int, input().split())

a, b = A, B
s1, s2 = 1, 0
t1, t2 = 0, 1

while b != 0:
    q = a // b

    r =a%b
    s = s1 - (s2 * q)
    t = t1 - (t2 * q)

    a = b
    b = r

    s1 = s2
    s2 = s

    t1 = t2
    t2 = t

print(s1, t1, a)

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

for i in range(len(s) - 1, 0, -1):
    if s[:i] == s[-i:]:
        print(s[:i])
        break
else:
    print("")

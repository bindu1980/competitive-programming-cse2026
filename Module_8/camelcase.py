# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
words=input().split(',')
pattern=input().strip()

def abbreviation(word):
    return ''.join(c for c in word if c.isupper())

matches=[]

for word in words:
    abbr=abbreviation(word)
    if abbr.startswith(pattern):
        matches.append((abbr,word))

matches.sort()

if not matches:
    print("No match found")
else:
    for abbr,word in matches:
        print(word)

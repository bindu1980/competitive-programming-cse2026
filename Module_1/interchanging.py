# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
arr=list(map(int, input().split()))
max_index = arr.index(max(arr))
min_index = arr.index(min(arr))
arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
print(*arr)

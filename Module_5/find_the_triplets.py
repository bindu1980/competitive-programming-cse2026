def triplets(arr,x):
    n = len(arr)
    for i in range(0, n):
        j = i + 1
        k = n - 1
        while j < k :
            if arr[i] + arr[j] + arr[k] == x:
                print(arr[i], arr[j], arr[k])
                j += 1
                k -= 1
            elif arr[i] + arr[j] + arr[k] < x:
                j += 1    
            elif arr[i] + arr[j] + arr[k] > x:
                k -= 1
            else:
                print('No Triplet Found')
n = int(input())
arr = list(map(int,input().split()))
x = int(input())
arr.sort()
triplets(arr,x)

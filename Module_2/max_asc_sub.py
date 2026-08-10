def maxAscendingSum(arr):
    max_sofar = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_sum += arr[i]
        else:
            current_sum = arr[i]

        if current_sum > max_sofar:
            max_sofar = current_sum

    return max_sofar

l = int(input())
arr = list(map(int, input().split()))
print(maxAscendingSum(arr))

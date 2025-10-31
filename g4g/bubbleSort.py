def bubbleSort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swap = True
        if not swap:
            break

    return arr


print(bubbleSort([41, 9, 9, 48, 11, 2, 11, 12, 28, 10, 15, 4, 16, 48]))

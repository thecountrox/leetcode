def selectionSort(arr):
    for i in range(len(arr)):
        _min = arr[i]
        _minplace = i
        for j in range(i, len(arr)):
            if _min > arr[j]:
                _min = arr[j]
                _minplace = j
        temp = arr[_minplace]
        arr[_minplace] = arr[i]
        arr[i] = temp
    return arr


print(selectionSort([5, 4, 3, 2, 1]))

from typing import List


def reverseString(s: List[str]) -> None:
    # inplace string changes
    def rev(arr, l, r):
        if l >= r:
            return

        arr[l], arr[r] = arr[r], arr[l]

        rev(arr, l + 1, r - 1)

    n = len(s)
    rev(s, 0, n - 1)


x = input("INPUT: ")
y = []
for i in range(len(x)):
    y.append(x[i])
reverseString(y)
print(y)

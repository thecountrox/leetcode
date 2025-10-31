"""
INPUT: 3

1         1
1 2     2 1
1 2 3 3 2 1
"""


def patt(n: int) -> None:
    gap = n * 4
    for i in range(n + 1):
        for j in range(i):
            print(j + 1, end=" ")
        for j in range(gap):
            print(" ", end="")
        gap -= 4
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


patt(int(input()))

def patt(n: int) -> None:
    gap = 4 * n - 4
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        for k in range(gap):
            print(" ", end="")

        for k in range(i + 1):
            print("*", end=" ")
        gap -= 4
        print()
    gap = 0
    lim = j
    for i in range(n - 1):
        for j in range(lim, i, -1):
            print("*", end=" ")
        gap += 4
        for k in range(gap):
            print(" ", end="")
        for k in range(lim, i, -1):
            print("*", end=" ")

        print()

    pass


patt(int(input()))

def patt(n: int) -> None:
    if n == 1:
        print("*")
        return
    gap = n - 2
    for i in range(n):
        print("*", end="")
    print()
    for i in range(n - 2):
        print("*", end="")
        for j in range(gap):
            print(" ", end="")
        print("*", end="")
        print()

    for i in range(n):
        print("*", end="")
    print()


patt(int(input()))

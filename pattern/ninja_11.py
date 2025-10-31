def patt(n: int) -> None:
    # Q1
    gap = 0
    for i in range(n):
        for j in range(n, i, -1):
            print("*", end=" ")

        # Q2
        # gap gen
        for k in range(gap):
            print(" ", end="")

        # actual gen
        for k in range(n, i, -1):
            print("*", end=" ")
        gap += 4
        print()

    gap -= 4
    # Q3
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")

        # gap gen
        for k in range(gap):
            print(" ", end="")
        gap -= 4

        # actual gen
        for k in range(i + 1):
            print("*", end=" ")
        # print("|", end="")
        print()


patt(int(input()))

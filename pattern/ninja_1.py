def star(n: int) -> None:
    gap = 0
    star = n * 2 - 1
    for i in range(n):
        for j in range(gap):
            print(" ", end="")
        for j in range(star):
            print("*", end="")
        star -= 2
        gap += 1
        print()


star(int(input()))

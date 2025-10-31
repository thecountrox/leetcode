def patt(n: int) -> None:
    num = 1
    for i in range(n):
        for j in range(i + 1):
            if j == i:
                print(num, end="")
            else:
                print(num, end=" ")
            num += 1
        print()


patt(int(input()))

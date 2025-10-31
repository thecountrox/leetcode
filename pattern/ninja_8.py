def patt(n: int) -> None:
    for i in range(n):
        num = "A"
        for j in range(i, 0, -1):

            if j == i:
                print(num, end="")
            else:
                print(num, end=" ")
            num = chr(ord(num) + 1)
        print()


patt(int(input()))

def patt(n: int) -> None:
    gap = n * 2 - 2
    for i in range(1, n + 1):
        for j in range(gap):
            print(" ", end="")

        ch = "A"
        for j in range(i):
            print(ch, end=" ")
            ch = chr(ord(ch) + 1)
        k = ord("A")
        v = ord(ch)
        for j in range(v - 1, k, -1):
            print(chr(j - 1), end=" ")

        print()
        gap -= 2


patt(int(input()))

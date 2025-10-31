def patt(n: int) -> None:
    base = ord("A")
    req = base + n - 1
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(req - j), end=" ")
        print()


patt(int(input()))

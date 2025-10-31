"""
3

1
0 1
1 0 1
"""


def patt(n: int) -> None:
    star = 1
    alt = 0
    for i in range(n):
        for j in range(star):

            if j == 0:
                if i % 2 == 0:
                    alt = 1
                else:
                    alt = 0
            if j == star - 1:
                print(alt, end="")
            else:
                print(alt, end=" ")
            if alt == 0:
                alt = 1
            else:
                alt = 0

        star += 1
        print()


patt(int(input()))

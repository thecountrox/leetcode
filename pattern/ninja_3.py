"""
Input: ‘N’ = 3
Output:
*
**
***
**
*
"""


def patt(n: int) -> None:
    star = 1
    for i in range(n):
        for j in range(star):
            print("*", end="")
        star += 1
        print()

    star -= 2
    for i in range(n):
        for j in range(star):
            print("*", end="")
        star -= 1
        print()


patt(int(input()))

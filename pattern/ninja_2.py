"""
Sample Input 1: 3
Sample Output 1:
  *
 ***
*****
*****
 ***
  *
Sample Input 2 : 1
Sample Output 2 :
*
*
"""


def patt(n: int) -> None:
    star = 1
    gap = (n * 2 - 1) // 2
    for i in range(n):
        for j in range(gap):
            print(" ", end="")

        for j in range(star):
            print("*", end="")
        star += 2
        gap -= 1
        print()

    star = n * 2 - 1
    gap = 0
    for i in range(n):
        for j in range(gap):
            print(" ", end="")

        for j in range(star):
            print("*", end="")
        star -= 2
        gap += 1
        print()


patt(int(input()))

def generateParenthesis(n: int) -> list[str]:

    res = []
    def genPairForN(o: int, c: int, s: str)-> None:

        if c == 0 and o == 0:
            res.append(s)
            return

        if o > 0:
            genPairForN(o - 1, c, s + '(')

        if c > 0 and o > c:
            genPairForN(o, c - 1, s + ')')

    genPairForN(n - 1,n,'')

    return res

print(generateParenthesis(3))

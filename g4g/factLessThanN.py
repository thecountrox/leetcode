def factN(n):

    def rec(n, i, x, lst):
        if i > n:
            return lst
        lst.append(i)
        i *= x + 1
        x += 1
        return rec(n, i, x, lst)

    lst = []
    return rec(n, 1, 1, lst)


print(factN(int(input())))

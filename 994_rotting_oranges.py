from typing_extensions import List


def orangesRotting(grid: List[List[int]]) -> int:

    def propogate(l: List[int]):
        i = l[0]
        j = l[1]

        if i - 1 >= 0 and grid[i - 1][j] == 1:
            grid[i - 1][j] = 2

        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            grid[i + 1][j] = 2

        if j - 1 >= 0 and grid[i][j - 1] == 1:
            grid[i][j - 1] = 2

        if j + 1 < len(grid) and grid[i][j + 1] == 1:
            grid[i][j + 1] = 2

    def checknearby(i: int, j: int):
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            return True

        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            return True

        if j - 1 >= 0 and grid[i][j - 1] == 1:
            return True

        if j + 1 < len(grid) and grid[i][j + 1] == 1:
            return True
        return False

    def checkrotten(grid: List[List[int]]):
        for i in grid:
            for j in i:
                if j == 1:
                    return False
        return True

    _stack = []
    cnt = 0

    # check if its already filled
    if checkrotten(grid):
        return 0

    while True:

        # 1 pass
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    if checknearby(i, j):
                        _stack.append([i, j])

        if len(_stack) == 0:
            if checkrotten(grid):
                if cnt == 0:
                    return -1
                else:
                    return cnt
            else:
                return -1
        else:
            cnt += 1
            print(_stack)

        while _stack:
            propogate(_stack.pop())  # [1,2]

        # if not checkrotten(grid):
        #     return -1
        # return cnt


print(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))

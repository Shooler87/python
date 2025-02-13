import collections
import random

import numpy as np


def init_grid():
    m = np.zeros((4, 4), dtype=int)
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    m[x, y] = 2

    while True:
        x2 = random.randint(0, 3)
        y2 = random.randint(0, 3)

        if x2 != x and y2 != y:
            m[x2, y2] = 2
            break

    return m


def add_new(grid):
    grid = np.copy(grid)
    zeros = np.where(grid == 0)
    if len(zeros) == 0:
        return grid

    r = random.randint(0, len(zeros[0]) - 1)
    grid[zeros[0][r], zeros[1][r]] = 2 * (2 if random.randint(1, 100) <= 20 else 1)
    return grid


def rollin_row(row):
    row_wo_0s = [x for x in row if x != 0]

    for i in range(len(row_wo_0s)):
        try:
            if row_wo_0s[i] == row_wo_0s[i + 1]:
                row_wo_0s[i] *= 2
                del row_wo_0s[i + 1]
        except IndexError:
            pass

    while len(row_wo_0s) < len(row):
        row_wo_0s.append(0)
    return row_wo_0s


def rollin(grid, direction):
    # print(direction)
    grid = np.copy(grid)
    if direction == "l":
        for row in range(len(grid)):
            grid[row] = rollin_row(grid[row])
    elif direction == "r":
        for row in range(len(grid)):
            grid[row] = rollin_row(grid[row][::-1])[::-1]
    elif direction == "u":
        for row in range(len(grid)):
            col = grid[:, row]
            grid[:, row] = rollin_row(col)
    elif direction == "d":
        for row in range(len(grid)):
            col = grid[:, row]
            grid[:, row] = rollin_row(col[::-1])[::-1]
    else:
        pass

    return grid


def not_lost(grid, direction):
    can_move = 0
    for d in "lrdu":
        # print("-------------------")
        # print(d)
        tmp = np.copy(grid)
        tmp2 = rollin(tmp, d)
        # print("cmp")
        # print(tmp)
        # print(tmp2)
        # print("-------------------")
        if (tmp == tmp2).all():
            if d == direction:
                pass
                # print("Stuck, choose other direction than " + d)
        else:
            can_move += 1
    if can_move > 0:
        # print("Can move in " + str(can_move) + " direction(s)")
        return True


results = []
while len(results) < 10000:
    grid = init_grid()
    # print(grid)
    while True:
        # direction = input("Choose direction [lrdu] or [q] to quit: ")
        direction = "lrdu"[random.randint(0, 3)]
        if direction in "lrdu":
            # print("direction:", direction)
            gridtmp = rollin(grid, direction)

            if not_lost(grid, direction):
                # grids not equal then add new element
                if not (grid == gridtmp).all():
                    grid = add_new(gridtmp)
                    # print(grid)
                    # sleep(0.1)
            else:
                results.append(np.max(grid))
                # print("GAME OVER")
                break
        elif direction == "q":
            print("You chose to quit")
            break
        else:
            print("Wrong input")
            continue

print(collections.Counter([int(x) for x in results if x >= 128]))

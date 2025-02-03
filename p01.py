import math

a = 5
b = 7
sumab = a + b
print(a + b)
print(f"{sumab}")


def draw_tree(height: int):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (i * 2 + 1))
    draw_trunk(height)


def draw_trunk(height: int):
    trunk_pos = math.ceil((2 * height - 1) / 2)
    for i in range(int(height / 2)):
        print(" " * (trunk_pos - 1) + "*")


draw_tree(7)

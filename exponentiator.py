def exponentiate(x, y):
    return pow(x, y)


def raise_to_fourth_power(x):
    return exponentiate(x, 4)


square = lambda x: x * x


cube = lambda x: pow(x,3)

print(square(2))

print(cube(2))

print(raise_to_fourth_power(2))


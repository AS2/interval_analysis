import intvalpy as iv

# one global min func
def booth(x):
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2

def booth_1(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2

def threeHumpCamelFunc(x):
    return 2 * (x[0] * x[0]) - 1.05 * (x[0] ** 4) + (x[0] ** 6) / 6 + x[0] * x[1] + x[1] * x[1]

# more than one global min func
def himmelblausFunc(x):
    return (x[0] * x[0] + x[1] - 11) ** 2 + (x[0] + x[1] * x[1] - 7) ** 2

def himmelblausFunc_1(x, y):
    return (x * x + y - 11) ** 2 + (x + y * y - 7) ** 2
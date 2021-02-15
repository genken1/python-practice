import math
from helpers import refactor_answer


def f11(x, y):
    return 64 * math.pow(y, 4) - x + \
           (math.pow(x, 4) + 94 * y) / ((math.pow(math.e, y) - math.pow(y, 2)) + 80) - \
           math.sqrt(math.tan(y) - 19 * math.pow(y, 7))


print(refactor_answer(f11(-24, -59)))
print(refactor_answer(f11(-75, -25)))

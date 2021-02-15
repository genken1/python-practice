import math
from helpers import refactor_answer


def f12(x):
    if x < -23:
        return 17 * x + math.pow(math.e, x)
    if (-23 <= x) and (x < 68):
        return math.log(math.tan(x) - math.tan(x) - 35) - math.sin(math.pow(x, 2) + math.pow(x, 5))
    if (68 <= x) and (x < 133):
        return math.pow(math.e, math.tan(29 * math.pow(x, 6))) + math.pow(x, 5)
    if (133 <= x) and (x < 195):
        return 47 * math.pow(x, 4) + x
    if x >= 195:
        return (94 * math.pow(x, 7) + 80 * math.pow(x, 6)) / 83 - math.cos(x)


print(refactor_answer(f12(177)))
print(refactor_answer(f12(77)))

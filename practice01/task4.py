import math
from helpers import refactor_answer


def f14(n):
    return 10 if n == 0 else math.sin(f14(n - 1)) - math.cos(f14(n - 1))


print(refactor_answer(f14(12)))
print(refactor_answer(f14(9)))

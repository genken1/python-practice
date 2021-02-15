import math
from helpers import refactor_answer


def f13(n, m):
    f_part = 0
    s_part_tmp = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f_part += math.pow(j, 7) + 5 * math.pow(j, 2) - 9
            s_part_tmp += 38 * math.pow(i, 4) - math.pow(j, 3) - 13

    return f_part - s_part_tmp / 77


print(refactor_answer(f13(76, 54)))
print(refactor_answer(f13(98, 15)))

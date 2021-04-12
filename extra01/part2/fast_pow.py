def fast_pow(x, y):
    res = 1

    while y > 0:
        if y == 1:
            return res * x
        if y % 2 != 0:
            res *= x
        y //= 2
        x *= x

    return res


def test_fast_pow():
    for x in range(101):
        for y in range(101):
            assert fast_pow(x, y) == pow(x, y)


test_fast_pow()
print(fast_pow(2, 5))

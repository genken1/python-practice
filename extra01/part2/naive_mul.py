def naive_mul(x, y):
    r = 0
    for _ in range(y):
        r += x

    return r


def test_naive_mul():
    for x in range(101):
        for y in range(101):
            assert naive_mul(x, y) == x * y


test_naive_mul()
print(naive_mul(10, 15))

def mul_12(x):
    t = x + x
    f = t + t
    e = f + f
    return e + f


def mul_16(x):
    t = x + x
    f = t + t
    e = f + f
    return e + e


def mul_15(x):
    t = x + x
    f = t + t
    e = f + f
    return e - (0 - e) - x


def mul_29(x):
    t = x + x
    f = t + t
    e = f + f
    s = e + e
    return s + s - (t + x)


print(mul_12(5))
print(mul_16(5))
print(mul_15(5))
print(mul_29(5))

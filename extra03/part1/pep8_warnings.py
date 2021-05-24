# Нарушения PEP 8

# 1. whitespace before '('.
# 4. unexpected spaces around keyword / parameter equals.
def calc (num = 0):

    # 2. missing whitespace around operator.
    res = 1+2

    # 5 expected 2 blank lines, found 1.


    # 3. missing whitespace after ','.
    b = [1,3,3]

    # 6. multiple statements on one line (colon).
    if a > 5: a = 10

    # 7. multiple statements on one line (semicolon).
    c = 5; d = 10

    return a, b, res

# 8. comparison to None should be 'if cond is None:'.
a = 1
a = a == None

# 9. comparison to True should be 'if cond is True:' or 'if cond:'.

a = a == True

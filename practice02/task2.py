def f22(x):
    a = (x & 0x3F) << 5
    b = (x & 0x1FC0) << 5
    c = (x & 0x7FFE000) << 5
    d = (x & 0x8000000) >> 27
    e = (x & 0xF0000000) >> 27
    return a + b + c + d + e


print(hex(f22(0x0306e165)))
print(hex(f22(0x55f3941f)))

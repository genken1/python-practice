from itertools import groupby


def bwt_encoded(line):
    table = [line[index:] + line[:index] for index, _ in enumerate(line)]
    table.sort()
    res = [row[-1] for row in table]
    return ''.join(res)


def bwt_decoded(line):
    table = [col for col in line]
    for i in range(len(line) - 1):
        table.sort()
        table = [line[i] + table[i] for i in range(len(line))]
    res = [row[-1] for row in table]
    res.append(res.pop(0))
    return ''.join(res)


def rle_encode(data):
    return [(k, len(list(g))) for k, g in groupby(data)]


if __name__ == '__main__':
    SEQUENCE = 'ABACABA'
    encode = bwt_encoded(SEQUENCE)
    decode = bwt_decoded(encode)
    print('Начальная последовательность', SEQUENCE)
    print('BWT кодирование:', encode)
    print('BWT декодирвоание:', decode)
    print('RLE кодирование', rle_encode(SEQUENCE))

from struct import unpack


def f31(binary_data):
    start_from = [int(i) for i in [0x45, 0x45, 0x46, 0x41]]
    # Получение id, с которого необходимо начать обработку
    idx = [
        (i, i + len(start_from)) for i in range(len(binary_data))
        if [int(i) for i in binary_data[i:i + len(start_from)]] == start_from
    ][0][1]

    def struct_a(index):
        response = {}
        # Размер (uint16) и адрес (uint16) массива char
        size, address = unpack('>HH', binary_data[index:index + 4])
        a1 = list(unpack('>{}b'.format(size), binary_data[address:address + size]))
        index += 4

        # Адрес (uint32) структуры B
        [a2] = unpack('>I', binary_data[index: index + 4])
        index += 4
        a2 = struct_b(a2)

        response['A1'] = ''.join([chr(x) for x in a1])
        response['A2'] = a2

        # Структура F
        response['A3'], index = struct_f(index)

        # int16
        response['A4'] = unpack('>h', binary_data[index: index + 2])[0]
        return response

    def struct_b(index):
        response = {}
        # Размер (uint16) и адрес (uint32) массива адресов (uint32) структур C
        size, address = unpack('>HI', binary_data[index:index + 6])
        index += 6
        addresses_arr = list(unpack('>{}I'.format(size), binary_data[address:address + 4 * size]))
        b1 = [struct_c(i) for i in addresses_arr]
        response['B1'] = b1

        # Структура D
        response['B2'], index = struct_d(index)

        # Адрес (uint32) структуры E
        [address_e] = unpack('>I', binary_data[index:index + 4])
        index += 4
        response['B3'] = struct_e(address_e)
        return response

    def struct_c(index):
        response = {}

        # uint8 int8
        c1, c2 = unpack('>Bb', binary_data[index:index + 2])
        index += 2

        # Массив uint8, размер 2
        c3 = list(unpack('>2B', binary_data[index: index + 2]))
        index += 2

        response['C1'] = c1
        response['C2'] = c2
        response['C3'] = c3
        return response

    def struct_d(index):
        response = {}
        # int32 int8 uint64
        d1, d2, d3 = unpack('>ibQ', binary_data[index:index + 13])
        index += 13

        # Массив int32, размер 3
        d4 = list(unpack('>3i', binary_data[index:index + 4 * 3]))
        index += 12

        # uint32
        [d5] = unpack('>I', binary_data[index:index + 4])
        index += 4
        response['D1'] = d1
        response['D2'] = d2
        response['D3'] = d3
        response['D4'] = d4
        response['D5'] = d5

        return response, index

    def struct_e(index):
        response = {}
        # double uint64 uint16 int64
        e1, e2, e3, e4 = unpack('>dQHq', binary_data[index:index + 26])
        index += 20
        response['E1'] = e1
        response['E2'] = e2
        response['E3'] = e3
        response['E4'] = e4
        return response

    def struct_f(index):
        response = {}
        # int16 int32 int32
        f1, f2, f3 = unpack('>hii', binary_data[index:index + 10])
        index += 10

        # Размер (uint16) и адрес (uint16) массива int16
        size, address = unpack('>HH', binary_data[index:index + 4])
        f4 = list(unpack('>{}h'.format(size), binary_data[address:address + 2 * size]))
        index += 4

        response['F1'] = f1
        response['F2'] = f2
        response['F3'] = f3
        response['F4'] = f4
        return response, index

    return struct_a(idx)

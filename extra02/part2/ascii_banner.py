# Разработать функцию, выдающую ASCII-баннер с пользовательским текстом.
def ascii_banner(text):
    arr = []
    i = 0

    with open('alphabet.txt') as file:
        read_file = file.read()
        line_split = read_file.split('@@')
    line_split.pop()

    for read_file in line_split:
        arr.append(read_file.split('@\n'))
        if arr[i][0][:1] == "\n":
            arr[i][0] = arr[i][0].replace('\n', '')
        i += 1

    for j in range(6):
        tmp = ''
        for i in range(len(text)):
            ind = ord(text[i])
            if 65 <= ind <= 90:
                tmp += arr[ind - 65][j]
            elif 97 <= ind <= 122:
                tmp += arr[ind - 71][j]
            elif 32 == ind:
                tmp += '    '
        print(tmp)


if __name__ == '__main__':
    ascii_banner('Python is a programming language')

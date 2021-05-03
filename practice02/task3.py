test = [
    ["092-133-0266#dilanz62@gmail.com", None, "68%", "68%"],
    ["016-384-7439#bozko49@yahoo.com", None, "50%", "50%"],
    ["882-592-8390#nigarberg57@yandex.com", None, "9%", "9%"],
    ["859-232-3233#fofadij36@mail.ru", None, "75%", "75%"],
]


def f23(table):
    # удаление пустых столбцов
    i = 0
    while i < len(table):
        j = 0
        while j < len(table[i]):
            if table[i][j] is None:
                del table[i][j]
                j -= 1
            j += 1
        i += 1

    # удаление дублирующихся постов
    i = 0
    while i < len(table):  # по строкам
        j = 0
        while j < len(table[i]):  # по столбцам
            k = j + 1
            while k < len(table[i]):  # по стобцам с шагом на единицу больше
                if table[i][j] == table[i][k]:
                    del table[i][k]
                    k -= 1
                k += 1
            j += 1
        i += 1

    for i in range(len(table)):
        person_data = table[i][0].split('#')
        phone_data = person_data[0].split('-', 1)
        code = phone_data[0]
        number = phone_data[1]
        domain = person_data[1].split('@')[1]
        per = round(int(table[i][1][:-1]) / 100, 1)
        table[i][0] = code + ' '+ number
        table[i][1] = str(per)
        table[i].append(domain)
    return table


print(f23(test))

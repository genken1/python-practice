# 1. Преобразовать элементы списка s из строковой в числовую форму.
def str_to_int(str_s):
    return [int(x) for x in str_s]


# 2. Подсчитать количество различных элементов в последовательности s.
def count_elem(s):
    return len(set(s))


# 3. Обратить последовательность s без использования функций.
def reverse(s):
    return s[::-1]


# 4 .Выдать список индексов, на которых найден элемент x в последовательности s.
def get_index(x, s):
    return [i for i in range(len(s)) if x == s[i]]


# 5. Сложить элементы списка s с четными индексами.
def sum_elem_even_index(s):
    return sum(s[1::2])


# 6. Найти строку максимальной длины в списке строк s.
def find_str_max_len(str):
    return max(str, key=len)


if __name__ == '__main__':
    assert str_to_int(["1", "2", "3", "4"]) == [1, 2, 3, 4]
    assert count_elem(["python", "task", "bonus", "python"]) == 3
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert get_index(7, [0, 7, 1, 7, 7, 2, 7]) == [1, 3, 4, 6]
    assert sum_elem_even_index([2, -178, -7, 67, 2, 78, 0, 19]) == -14
    assert find_str_max_len(["bonus", "python", "task", "practice"]) == "practice"

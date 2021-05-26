# 1. Преобразовать элементы списка s из строковой в числовую форму.
def to_int(str_s):
    return [int(x) for x in str_s]


# 2. Подсчитать количество различных элементов в последовательности s.
def count_elem(s):
    return len(set(s))


# 3. Обратить последовательность s без использования функций.
def reverse(s):
    return s[::-1]


# 4 .Выдать список индексов, на которых найден элемент x в последовательности s.
def get_all_indices_where_equal_x(x, s):
    return [i for i in range(len(s)) if x == s[i]]


# 5. Сложить элементы списка s с четными индексами.
def sum_elem_even_index(s):
    return sum(s[1::2])


# 6. Найти строку максимальной длины в списке строк s.
def find_str_of_max_len(str):
    return max(str, key=len)


if __name__ == '__main__':
    assert to_int(["1", "2"]) == [1, 2]
    assert count_elem(["one", "two"]) == 2
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert get_all_indices_where_equal_x(4, [4, 2, 3, 4, 5]) == [0, 3]
    assert sum_elem_even_index([1, -1, 2, 3, -5, 6, 7, 8]) == 16
    assert find_str_of_max_len(["one", "two", "three", "four", "python"]) == "python"

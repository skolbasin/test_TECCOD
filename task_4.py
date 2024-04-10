from typing import List


# В зависимости от задач, можно применить 3 варианта сортировки

# Через sorted
def sort_strings_by_length(strings: List) -> List:
    sorted_asc = sorted(strings, key=len)  # Сортировка по возрастанию длины
    sorted_desc = sorted(strings, key=len, reverse=True)  # Сортировка по убыванию длины
    return sorted_asc, sorted_desc


# Через sort
def sort_strings_by_length2(strings: List) -> List:
    strings.sort(key=len)  # Сортировка по возрастанию длины
    sorted_desc = sorted(strings, key=len, reverse=True)  # Сортировка по убыванию длины
    return strings, sorted_desc


# Через lambda
def sort_strings_by_length3(strings: List) -> List:
    return sorted(strings, key=lambda x: len(x)) + sorted(strings, key=lambda x: len(x), reverse=True)


# Проверка
strings = ["525252", "один", "гусеница", "лошадь", "pear"]
sorted_asc, sorted_desc = sort_strings_by_length(strings)
print(sorted_asc)
print(sorted_desc)

sorted_asc2, sorted_desc2 = sort_strings_by_length2(strings)
print(sorted_asc2)
print(sorted_desc2)

sorted_strings3 = sort_strings_by_length3(strings)
print(sorted_strings3)

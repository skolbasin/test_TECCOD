from typing import List


# У первой задача есть несколько вариантов решения.
# Самый базовые: создать из списка - множество.
# Почему? Потому что множество - тот же список, только с уникальными значениями
def unique_elem_1(input_list: List) -> List:
    return list(set(input_list))


# Но есть и второй. Он подойдет в том случае, если нам важен порядок элементов. Правда код получается более громоздким

def unique_elem_2(input_list: List) -> List:
    unique_list = []
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


# Проверка работы функций
test_list = [1, 2, 3, 2, 4, 5, 1]
print(unique_elem_1(test_list))
print(unique_elem_2(test_list))

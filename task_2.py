from typing import List
# В данной задаче можно было бы всё положить в одну функцию и выглядело бы примерно всё так:


def prime_numbers_in_range(min_number: int, max_number: int) -> List:
    prime_numbers = []
    for num in range(max(min_number, 2), max_number + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers


# Но если нам важен KISS, то правильнее было бы разложить всё на 2 функции:

def is_prime(num: int) -> bool:
    """
    Функция проверяет, является ли число простым.

    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers(min_number: int, max_number: int) -> List:
    """
    Функция возвращает список всех простых чисел в заданном диапазоне.

    """
    prime_num = []
    for num in range(min_number, max_number + 1):
        if is_prime(num):
            prime_num.append(num)
    return prime_num

# Проверка работы 1-го варианта
min_num = 10
max_num = 30

print(prime_numbers_in_range(min_num, max_num))

# Проверка работы 2-го варианта

print(prime_numbers(min_num, max_num))
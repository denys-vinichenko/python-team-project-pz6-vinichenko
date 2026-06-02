def calculate_average(numbers):
    """
    Обчислює середнє арифметичне.
    :param numbers: список числових значень
    :return: середнє арифметичне
    """
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """
    Обчислює медіану списку чисел.
    :param numbers: список числових значень
    :return: медіана
    """
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    middle = count // 2
    if count % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    return sorted_numbers[middle]


def calculate_minimum(numbers):
    """
    Знаходить мінімальне значення.
    :param numbers: список числових значень
    :return: мінімальне значення
    """
    return min(numbers)


def calculate_maximum(numbers):
    """
    Знаходить максимальне значення.
    :param numbers: список числових значень
    :return: максимальне значення
    """
    return max(numbers)


def calculate_statistics(numbers):
    """
    Перевіряє дані та обчислює основні статистичні показники.
    :param numbers: список числових значень
    :return: словник зі статистичними показниками
    :raises ValueError: якщо список чисел порожній
    """
    if not numbers:
        raise ValueError("Список чисел порожній")
    return {
        "Середнє значення": calculate_average(numbers),
        "Медіана": calculate_median(numbers),
        "Мінімум": calculate_minimum(numbers),
        "Максимум": calculate_maximum(numbers),
    }

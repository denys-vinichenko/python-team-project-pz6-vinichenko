def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    middle = count // 2

    if count % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    return sorted_numbers[middle]


def calculate_minimum(numbers):
    return min(numbers)


def calculate_maximum(numbers):
    return max(numbers)


def calculate_statistics(numbers):
    if not numbers:
        raise ValueError("Список чисел порожній")

    return {
        "Середнє значення": calculate_average(numbers),
        "Медіана": calculate_median(numbers),
        "Мінімум": calculate_minimum(numbers),
        "Максимум": calculate_maximum(numbers),
    }

def read_numbers(filename):
    """
    Зчитує числові значення з текстового файлу.
    :param filename: назва файлу з вхідними даними
    :return: список числових значень
    """
    numbers = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                # Некоректні рядки пропускаються, щоб програма не зупинялась.
                print(f"Пропущено некоректне значення: {line.strip()}")
    return numbers

def save_results(filename, results):
    """
    Зберігає результати статистичних обчислень у файл.
    :param filename: назва файлу для збереження результатів
    :param results: словник зі статистичними показниками
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")

from io_utils import read_numbers, save_results
from statistics_utils import calculate_statistics

def main():
    """
    Запускає програму, зчитує дані, обчислює статистику та зберігає результат.
    :return: None
    """
    input_file = "data.txt"
    output_file = "results.txt"

    numbers = read_numbers(input_file)
    results = calculate_statistics(numbers)

    print("Результати обчислень:")
    for key, value in results.items():
        print(f"{key}: {value}")
    save_results(output_file, results)

if __name__ == "__main__":
    main()

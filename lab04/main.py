import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    # Читаем все строки из стандартного ввода
    lines = sys.stdin.read().splitlines()

    # Извлекаем корректные записи
    valid_records = read_valid(lines)

    # Получаем количество ошибок из атрибута функции
    errors_count = getattr(read_valid, 'errors_count', 0)

    # Считаем средние температуры и ищем самый теплый город
    averages = average_by_city(valid_records)
    best_city = warmest_city(valid_records)

    # Получаем среднюю температуру лучшего города (или 0.0, если данных нет)
    best_temp = averages.get(best_city, 0.0)

    # Печать строго по ТЗ: 3 строки
    print(len(valid_records))
    print(errors_count)
    print(f"{best_temp:.1f}")


if __name__ == "__main__":
    main()
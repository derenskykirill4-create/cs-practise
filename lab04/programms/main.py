import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    # Читаем все строки из стандартного ввода
    lines = sys.stdin.read().splitlines()

    # Обрабатываем строки
    valid_records = read_valid(lines)
    errors_count = getattr(read_valid, 'invalid_count', 0)

    # Вычисляем финальные метрики
    averages = average_by_city(valid_records)
    best_city = warmest_city(valid_records)

    # Извлекаем температуру самого теплого города
    best_temp = averages.get(best_city, 0.0)

    # Печать строго в три строки, как требует условие
    print(len(valid_records))
    print(errors_count)
    print(f"{best_temp:.1f}")


if __name__ == "__main__":
    main()
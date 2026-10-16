import sys
from stats import read_valid, average_by_city, warmest_city


def main():
    # Читаем все строки из стандартного ввода
    lines = sys.stdin.read().splitlines()

    # Фильтруем данные и считаем ошибки
    valid_records, errors_count = read_valid(lines)

    # Выводим количество успешно разобранных записей
    print(len(valid_records))

    # Выводим количество строк с ошибками
    print(errors_count)

    # Если есть корректные записи, считаем результаты
    if valid_records:
        best_city = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        # Выводим среднюю температуру самого тёплого города с одним знаком после точки
        print(f"{averages[best_city]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()
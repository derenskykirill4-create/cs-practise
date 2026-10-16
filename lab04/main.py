import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    valid_records = read_valid(lines)

    # Подсчёт пропущенных строк (можно вести счётчик отдельно, здесь для наглядности)
    total_lines = len(lines)
    skipped_count = total_lines - len(valid_records)

    print(f"Всего строк: {total_lines}")
    print(f"Корректных записей: {len(valid_records)}")
    print(f"Строк с ошибками: {total_lines - len(valid_records)}")

    if valid_records:
        warmest = warmest_city(valid_records)
        avg_temp = average_by_city(valid_records)[warmest]
        print(f"Самый тёплый город: {warmest} (средняя температура: {avg_temp:.1f})")
    else:
        print("Нет корректных записей для расчёта.")

if __name__ == "__main__":
    main()

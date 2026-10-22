import sys
from logstats import count_levels, top_errors, format_report


def main():
    # Читаем имя файла строго из первой строки ввода без лишних проверок
    file_name = input().strip()

    # Первый проход: считаем количество строк по уровням
    with open(file_name, "r", encoding="utf-8") as log:
        counts = count_levels(log)

    # Второй проход: выбираем частые ошибки уровня ERROR
    with open(file_name, "r", encoding="utf-8") as log:
        errors = top_errors(log, n=3)

    # Считаем сумму только тех строк, которые содержали данные (все уровни + BROKEN)
    total_processed = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    # Печать строго трех чисел по условию задачи
    print(total_processed)
    print(error_count)
    print(broken_count)

    # Запись форматированного отчета
    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)


if __name__ == "__main__":
    main()
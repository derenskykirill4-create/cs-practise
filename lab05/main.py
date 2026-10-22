import sys
from logstats import count_levels, top_errors, format_report


def main():
    # Читаем имя файла журнала из первой строки ввода
    file_name = input().strip()

    # Чтобы не загружать весь файл в память, мы можем открыть его дважды
    # (два последовательных прохода по диску эффективнее, чем readlines() для больших файлов)

    # Проход 1: Подсчет уровней
    with open(file_name, "r", encoding="utf-8") as log_file:
        counts = count_levels(log_file)

    # Проход 2: Поиск самых частых ошибок (топ-3)
    with open(file_name, "r", encoding="utf-8") as log_file:
        errors = top_errors(log_file, 3)

    # Вычисляем агрегированные показатели для вывода на экран
    # Всего разобрано строк = сумма всех валидных уровней + BROKEN
    total_parsed = sum(counts.values())
    error_count = counts["ERROR"]
    broken_count = counts["BROKEN"]

    # Выводим в консоль три числа через пробел
    print(f"{total_parsed} {error_count} {broken_count}")

    # Формируем отчёт и записываем в report.txt рядом со скриптом
    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)


if __name__ == "__main__":
    main()